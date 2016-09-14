#from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    block_infos = [{"name": "北京机房Nagios", "urls": "http://10.21.2.4/nagios/"},
		   {"name": "佛山机房Nagios", "urls": "http://10.220.0.166/nagios/"},
		   {"name": "东莞机房Nagios", "urls": "http://119.147.156.122/nagios/"},
		   {"name": "北京机房NagiosQL", "urls": "http://10.21.2.4/nagiosql/"},
		   {"name": "佛山机房NagiosQL", "urls": "http://10.220.0.166/nagiosql/"},
		   {"name": "东莞机房NagiosQL", "urls": "http://119.147.156.122/nagadmin/"},
		   {"name": "北京机房Cacti", "urls": "http://10.21.2.4/cacti/index.php"},
		   {"name": "佛山机房Cacti", "urls": "http://10.220.2.224/cacti/index.php"},
		   {"name": "东莞机房Cacti(流量)", "urls": "http://119.147.156.57/newcacti/index.php"},
		   {"name": "上海机房CES", "urls": "http://10.22.1.254/centreon/main.php"},
		   {"name": "公司CES", "urls": "http://192.168.1.171/centreon/", "color": "0"},
		   {"name": "东莞机房CES(迁移中)", "urls": "http://10.11.2.200:8088/centreon/index.php"},
		   {"name": "公司2楼机房UPS", "urls": "http://192.168.1.236/indexnet.asp"},
		   {"name": "公司4楼机房UPS", "urls": "http://192.168.1.237/indexnet.asp"}
		  ]
    return render(request, "index.html", {"blocks": block_infos})

def monitor(request):
    return render(request, "monitor.html")
