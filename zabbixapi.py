# -*- coding: UTF-8 -*-
from pyzabbix import ZabbixAPI
import json
import ReportHtml as rhtml
import datetime,time
import os

class getzabbix():
	
	#获取zabbix数据
	def serverget(self):
		print('开始抓取zabbix数据')
		#通过API登录Zabbix
		ZABBIX_SERVER = 'http://127.0.0.1/zabbix'
		zapi = ZabbixAPI(ZABBIX_SERVER)
		try:
			zapi.login('liuchengxian', 'xxxxxxxxxx')
		except Exception:
			print('连接超时，请检查网络！')
			exit()

		#获取主机信息
		host_list = zapi.host.get(
			selectGroups="extend",
			output="extend",
			filter={
				'status':'0',
			},
		)

		#获得所有Linux、Winserver组下的主机ID和系统类型
		lmserver={}
		for i in host_list:
			for j in i['groups']:
				if j['name'] == 'Linux servers' or j['name'] == 'windows Server':
					lmserver[i['hostid']] = j['name']

		diskinfo = {}
		#获得Linux组下的主机的磁盘item值
		for i,stype in lmserver.items():
			item_list = zapi.item.get(
				hostids=i,
				output='extend',
				search={
					"key_":'vfs.fs.size',
				},
			)
			#截取和过滤盘符与值
			disktype=[]
			diskall=[]
			for j in item_list:
				if ',free' in j['key_']:
					continue
				disktype.append(j['key_']+':'+j['lastvalue'])
			for key in disktype:
				diskall.append(key.split('[')[1].split(',')[0])
				diskall.append(key.split('[')[1].split(':')[-1])
			#去掉盘符重复值写入l2列表
			l2 = []
			for de in diskall:
				try:
					if float(de) or int(de) == 0:
						l2.append(de)
				except ValueError:
					if de in l2:
						continue
					else:
						l2.append(de)

			#如果盘符不是4的倍数([c,pfree,total,used])就提示报错并跳过
			if len(l2) % 4 != 0:
				print("%s: 信息错误" % i)
				continue

			#获取IP和名称
			ipname = zapi.host.get(
				hostids = i,
				selectInterfaces=['ip'],
				output="extend",
				search={
					"key_":'system.uname',
				},
			)
			#将主机信息加入字典
			ihost=ipname[0]['host']
			iip=ipname[0]['interfaces'][0]['ip']

			#l4列表存储的是：分区，总大小，已用大小，可用大小,单位为GB,已用百分比
			l4=[]
			inde=1
			for h in l2:
				if inde%4==0:
					try:
						l3=[l2[inde-4],round(float(l2[inde-2])/1073741824,2),round(float(h)/1073741824,2)]
					except Exception:
						print("%s出现异常,已跳过" % ihost)
						continue
					freesize=round(l3[1]-l3[2],2)
					if l3[1] == 0 or l3[2] == 0:
						usedszie = 0
					else:
						usedszie=int(round(l3[2]/l3[1],2)*100)
					#写入剩余空间、已用百分比、系统类型、IP地址到l3列表
					l3.append(freesize)
					l3.append(usedszie)
					l3.append(stype)
					l3.append(iip)
					l4.append(l3)
				inde = inde + 1
			if len(l4) != 0:
				diskinfo[ihost] = l4
		#按照json格式写入文件
		json_str = json.dumps(diskinfo,indent=4)
		with open('test_data.json', 'w') as json_file:
			json_file.write(json_str)
		return diskinfo

	#格式化数据生成报表
	def serverinit(self):
		print('开始生成HTML报表')
		#读取json文件获取磁盘信息
		with open('test_data.json', 'r') as f:
			allinfo = json.load(fp=f)
		#indx作为有多少台服务器的变量，linuxlist存储Linux系统html，lincount存储Linux系统计数
		indx=1
		linuxlist=[]
		winlist=[]
		wincount=''
		lincount=''
		run_time =  datetime.datetime.now().strftime("%H:%M")
		#存储告警信息
		temp=''
		#统计Linux系统，生成html文本
		for key,value in allinfo.items():
			#iner作为有多少个盘符的变量
			iner=1
			break_flag=False
			colour=''
			status='OK'
			#循环每个盘符
			for values in value:
				if float(values[4]) >= 90:
					colour='bgcolor="#FF0000"'
					#超过阈值就写入html报表的Summer告警
					temp = temp + '<p><a href="#windows"> Alarm: 【{dbname}】 partition {disk} usage has exceeded {vau}%</a></p>'.format(dbname=key,disk=values[0],vau=values[4])
					status='Critical'
				elif float(values[4]) >= 80:
					colour='bgcolor="#FFFF00"'
					status='Warning'
				else:
					colour=''
					status='OK'
				#如果是第一行，就根据有多少个盘符来决定合并rowspan多少行
				#break_flag的作用是保证最外层的ID能根据每个IP来增加
				if iner == 1:
					if values[5] == 'Linux servers':
						linuxlist.append('<tr class=\'failClass warning\'><td rowspan="{}" align="center">{}</td><td rowspan="{}" align="center">{}</td><td rowspan="{}" align="center">{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td {}>{}%</td><td>{}</td><td>{}</td></tr>'.format(len(value),indx,len(value),key,len(value),values[6],values[0],values[1],values[2],values[3],colour,values[4],status,run_time))
						break_flag=True
				else:
					if values[5] == 'Linux servers':
						linuxlist.append('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td {}>{}%</td><td>{}</td><td>{}</td></tr>'.format(values[0],values[1],values[2],values[3],colour,values[4],status,run_time))
						break_flag=True
				iner+=1
			if break_flag == True:
				indx+=1
		lincount=str(int(indx)-1)
		#统计Windows系统，生成html文本
		indx=1
		for key,value in allinfo.items():
			#iner作为有多少个盘符的变量
			iner=1
			break_flag=False
			status='OK'
			for values in value:
				#判断如果值超过了阈值就改变表格颜色
				if float(values[4]) >= 90:
					colour='bgcolor="#FF0000"'
					status='Critical'
				elif float(values[4]) >= 80:
					colour='bgcolor="#FFFF00"'
					status='Warning'
				else:
					colour=''
					status='OK'
				if iner == 1:
					if values[5] == 'windows Server':
						winlist.append('<tr class=\'failClass warning\'><td rowspan="{}" align="center">{}</td><td rowspan="{}" align="center">{}</td><td rowspan="{}" align="center">{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td {}>{}%</td><td>{}</td><td>{}</td></tr>'.format(len(value),indx,len(value),key,len(value),values[6],values[0],values[1],values[2],values[3],colour,values[4],status,run_time))
						break_flag=True
				else:
					if values[5] == 'windows Server':
						winlist.append('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td {}>{}%</td><td>{}</td><td>{}</td></tr>'.format(values[0],values[1],values[2],values[3],colour,values[4],status,run_time))
						break_flag=True
				iner+=1
			if break_flag == True:
				indx+=1
		wincount=str(int(indx)-1)
		#将格式化的数据转换成字符串方便与html结合
		winaix=''
		for i in winlist:
			winaix = winaix + '\r' + i

		linaix=''
		for i in linuxlist:
			linaix = linaix + '\r' + i

		#调取html模板
		html = rhtml.ReHtml()

		#格式化时间
		now_time = getzabbix().get_day(datetime.datetime.now())
		now_time1 = datetime.datetime.now().strftime("%Y-%m-%d")
		time_h =  datetime.datetime.now().strftime("%H")
		now_time2 = "{}, {} {}, {} {}".format(now_time[0],now_time[1],now_time[2],now_time[3],now_time[4])
		log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")		

		#调用HTML模板，把前面获取的数据添加到HTML模板中，使其成为完整的报表
		#生成HTML    
		output = html.HTML_Report % dict(
			linux_r = linaix,
	        windows_r = winaix,
	        now_time_aix_1 = now_time1,
	        now_time_aix_2 = now_time2,
	        message = temp,
	        lincount = lincount,
	        wincount = wincount,
	        )
		#生成html报告
		with open("report_tmp.html",'wb') as f:
			f.write(output.encode('utf-8'))

	#生成特定时间函数
	def get_day(self,date):
		week_day_dict = {
			0 : 'Monday',
			1 : 'Tuesday',
			2 : 'Wednesday',
			3 : 'Thursday',
			4 : 'Friday',
			5 : 'Saturday',
			6 : 'Sunday',
		}
		month_day_dict = {
			1 : 'Janurary',
			2 : 'February',
			3 : 'March',
			4 : 'April',
			5 : 'May',
			6 : 'June',
			7 : 'July',
			8 : 'August',
			9 : 'September',
			10 : 'October',
			11 : 'November',
			12 : 'December',
		}
		week_day = date.weekday()
		month_day = date.month
		day = date.day
		year = date.year
		dtime = datetime.datetime.now().strftime("%H:%M:%S %p")
		#返回值：Tuesday, November 20, 2018 13:10:02 PM
		return week_day_dict[week_day],month_day_dict[month_day],day,year,dtime

if __name__ == '__main__':
	a = getzabbix()
	a.serverget()
	a.serverinit()

