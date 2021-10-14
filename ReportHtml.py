# -*- coding: UTF-8 -*-
class ReHtml(object):
	"""html报告"""
	HTML_Report = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">	
	<html>
<head>
	<title>LEEMAN SERVER REPORT</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta http-equiv="Content-Style-Type" content="text/css" />
	<meta name="author" content="LEEMAN SERVER REPORT" />
	<meta name="description" content="LEEMAN SERVER REPORT" />
	<style type="text/css">
	body {
	font-family: tahoma, helvetica, arial, sans-serif;
	font-size: 0.8em;
	color: #333;
	background-color: White;
	padding: 0;
	margin: 0;
}
a {
  text-decoration: none
}
p{
  font-size:90%%
}
h1 {
   font-weight: normal;
   font-size: x-large;
   background-color: #000066;
   color: White;
   padding: 0.5em 0.5em 0 0.5em;
   margin: 0;
}
h5 {
	border-bottom-color: #6666CC;
	border-bottom-style: solid;
	border-bottom-width: medium;
	background-color: #000066;
	font-weight: normal;
	font-size: small;
	background-color: #000066;
	color: White;
	padding: 0 1em 0.5em 1em;
	margin: 0;
}
h2 {
	line-height: 40px;
	color: #000066;
	margin-top: 2em;
	margin-bottom: 0.5em;
	font-size: large;
}

h3 {
	color: #000066;
	margin-top: 2em;
	margin-bottom: 0.5em;
	font-size: large;
}
ul {
	line-height: 1.5em;}
#content {
	font-size: medium;
	padding-left: 1em;
	padding-right: 1em;
}
#footer {
	background-color: #DDDDDD;
	color: Black;
	font-size: x-small;
	text-align: center;
}
.facsevtable2 {
	margin-left: 2em;
	text-align: left;
	border-top: thin solid #666633;
	border-bottom: thin solid #666633;
	width: 95%%;
	border-collapse: collapse;
	font-size: small;
}
.facsevtable2 tr {
	height: 1.5em;
}
.facsevtable2 td {
	border-right: 1px dotted #CCCC99;
	border-bottom: 1px dotted #CCCC99;
	vertical-align: top;
	padding-left: 3px;
}
.m_col {
	font-size: smaller;
}
.f_col {
	width:8%%;
}
.row_hl {
	background-color: #f6f6ed;
}
.facsevtable2 th {
	font-weight: bold;
	margin-left: 1em;
	font-weight: normal;
	background-color: #CCCC99;
	border-right: 1px dotted White;
	border-bottom: 1px dotted White;
	padding-left: 3px;
}
img { 
	border: 0 none; 
}
.facsevtable {
	text-align: center;
	border-top: medium solid #666633; 
	border-bottom: thin solid #666633; 
	width: 100%%;
	border-collapse: collapse;
}

.facsevtable tr {
	height: 1.5em;
}


.facsevtable td {
	width: 8%%;
	font-size: smaller;
	border-right: thin solid #CCCC99;
	border-bottom: thin solid #CCCC99;
}

.facsevtable th {
	font-size: smaller;
	font-weight: normal;
	background-color: #CCCC99;
	border-right: thin solid White;
	border-bottom: thin solid White;
}

img { 
	border: 0 none; 
}

.righttable {
	text-align: center;
	border-top: medium solid #666633; 
	border-bottom: thin solid #666633; 
	width: 100%%;
	border-collapse: collapse;
}

.righttable tr {
	height: 1.5em;
	font-size: smaller;
}

.righttable td {
	border-right: thin solid #CCCC99;
	border-bottom: thin solid #CCCC99;
}

.righttable th {
	font-weight: normal;
	background-color: #CCCC99;
	border-right: thin solid White;
	border-bottom: thin solid White;
}

.twintable {
	border: none;
	width: 100%%;
}

.twintable td {
	vertical-align: middle;
	text-align: center;
}

.picdescr {
	font-size: smaller;
	font-style: italic;
}
#customers
  {
  font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
  width:70%%;
  border-collapse:collapse;
  word-wrap:break-word;
  margin-left:1em;
  }

#customers td, #customers th 
  {
  border-collapse:collapse;
  font-size:0.8em;
  border:1px solid #98bf21;
  padding:3px 7px 2px 7px;
  max-height:50px
  }

#customers th 
  {
  font-size:1em;
  text-align:left;
  padding-top:5px;
  padding-bottom:4px;
  background-color:#A7C942;
  color:#ffffff;
  }

#customers tr.alt td 
  {
  color:#000000;
  background-color:#EAF2D3;
  }
  
#customerss
  {
  font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
  width:94%%;
  border-collapse:collapse;
  word-wrap:break-word;
  margin-left:1em;
  }
 #cus_head
  {
  font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
  width:20%%;
  border-collapse:collapse;
  word-wrap:break-word;
  margin-left:1em;
  }
 #cus_head td
  {
  border-collapse:collapse;
  font-size:0.5em;
  border:1px solid #98bf21;
  padding:3px 7px 2px 7px;
  max-height:50px
  }
 #cus_head tr.alt td 
  {
  color:#ffffff;
  background-color:#EAF2D3;
  }
 #cus_title
  {
  font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
  width:20%%;
  border-collapse:collapse;
  word-wrap:break-word;
  margin-left:1em;
  }
 #cus_title td
  {
  border-collapse:collapse;
  font-size:2em;
  border:1px solid #98bf21;
  padding:3px 7px 2px 7px;
  max-height:50px
  }
 #cus_title tr.alt td 
  {
  color:#ffffff;
  background-color:#EAF2D3;
  }

#customerss td, #customerss th 
  {
  border-collapse:collapse;
  font-size:0.8em;
  border:1px solid #98bf21;
  padding:3px 7px 2px 7px;
  max-height:50px
  }

#customerss th 
  {
  font-size:1em;
  text-align:left;
  padding-top:10px;
  padding-bottom:4px;
  background-color:#A7C942;
  color:#ffffff;
  }

#customerss tr.alt td 
  {
  color:#000000;
  background-color:#EAF2D3;
  } 

#box_relative {
  position: fixed;
  left: 35px;
  top: 350px;
}
</style>
  <script language="JavaScript">
    function isHidden(oDiv){
      var vDiv = document.getElementById(oDiv);
      vDiv.style.display = (vDiv.style.display == 'none')?'block':'none';
    }
  </SCRIPT>
</head>

 <body>
	<h1>LEEMAN SERVER DAILY CHECK REPORT (%(now_time_aix_1)s)</h1>
	<h5>Report generated at %(now_time_aix_2)s</h5>
	<div id="content">

<DIV style="cursor:hand" onclick="isHidden('div12')">
<h2>Summary</h2>
</DIV>
<div id='div12'>
<ul>
<li>
<b>Server Count Check Report</b>
<p>
<a href="#linux">Linux Server Count: [ %(lincount)s ]</a>
</p>
<p>
<a href="#windows">Windows Server Count: [ %(wincount)s ]</a>
</p>
</li>
<li>
<b>Storage Disk Daily Check Report</b>
%(message)s
</li>
</ul>
</div>
	
<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>
<a name="linux"></a>
<DIV style="cursor:hand" onclick="isHidden('div1')">
<table id='cus_title' class="table table-condensed table-bordered table-hover">
			<tr class='failClass warning'>
				<td align="center" bgcolor="#F8F8FF">Linux Server</td>
			</tr>			
</table>
</DIV>
<DIV id="div1">
<table id='cus_head' class="table table-condensed table-bordered table-hover">
			<tr class='failClass warning'>
				<td rowspan="3" align="center" bgcolor="CCFF00">Disk Usage</td>
				<td bgcolor="#00FF00">Normal</td>
				<td bgcolor="#F8F8FF"><80%%</td>
			</tr>
			<tr class='failClass warning'>
				<td bgcolor="#FFFF00">Warning</td>
				<td bgcolor="#F8F8FF">>80%% and <90%%</td>
			</tr>
			<tr class='failClass warning'>
				<td bgcolor="#FF0000">Critical</td>
				<td bgcolor="#F8F8FF">>90%%</td>
			</tr>			
</table>
<table id='customerss' class="table table-condensed table-bordered table-hover" >
		<colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
				<tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th>Number</th>
                    <th>Server name</th>
                    <th>IPAddr</th>             
					<th>Disk label</th>
					<th>Total_size(GB)</th>
					<th>Used_size(GB)</th>
					<th>Free size(GB)</th>
					<th>Usage(%%)</th>
					<th>Running status</th>
					<th>Check Time</th>
                </tr>
				%(linux_r)s
				</table>
</DIV>

<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>
<a name="windows"></a>
<DIV style="cursor:hand" onclick="isHidden('div2')">
<table id='cus_title' class="table table-condensed table-bordered table-hover">
			<tr class='failClass warning'>
				<td align="center" bgcolor="#F8F8FF">Windows Server</td>
			</tr>			
</table>
</DIV>
<DIV id="div2">
<table id='cus_head' class="table table-condensed table-bordered table-hover">
			<tr class='failClass warning'>
				<td rowspan="3" align="center" bgcolor="CCFF00">Disk Usage</td>
				<td bgcolor="#00FF00">Normal</td>
				<td bgcolor="#F8F8FF"><80%%</td>
			</tr>
			<tr class='failClass warning'>
				<td bgcolor="#FFFF00">Warning</td>
				<td bgcolor="#F8F8FF">>80%% and <90%%</td>
			</tr>
			<tr class='failClass warning'>
				<td bgcolor="#FF0000">Critical</td>
				<td bgcolor="#F8F8FF">>90%%</td>
			</tr>			
</table>
<table id='customerss' class="table table-condensed table-bordered table-hover" >
		<colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
				<tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th>Number</th>
                    <th>Server name</th>
                    <th>IPAddr</th>                      
					<th>Disk label</th>
					<th>Total_size(GB)</th>
					<th>Used_size(GB)</th>
					<th>Free size(GB)</th>
					<th>Usage(%%)</th>
					<th>Running status</th>
					<th>Check Time</th>
                </tr>
				%(windows_r)s
				</table>
</DIV>

<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>


</body>
</html>
	
	'''