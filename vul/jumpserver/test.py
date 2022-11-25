import re
import json

def fun(par):	# 传入data
	print("## %s:"%par的原变量名,type(par))
	# print("## data:",type(data))
	
data='''
{
	"list":[
	{"message":"172.17.0.3 [28/Mar/2022:23:59:19 +0800] POST /api/v1/terminal/terminals/status/?from_guacamole=1 HTTP/1.1"},
	{"message":"172.17.0.2 [28/Mar/2022:23:59:21 +0800] POST /api/v1/terminal/terminals/status/ HTTP/1.1"},
	{"message":"172.17.0.3 [28/Mar/2022:23:59:29 +0800] POST /api/v1/terminal/terminals/status/?from_guacamole=1 HTTP/1.1"},
	{"message":"172.17.0.2 [28/Mar/2022:23:59:33 +0800] GET /api/v1/terminal/terminals/config/ HTTP/1.1"},
	{"message":"172.17.0.3 [28/Mar/2022:23:59:39 +0800] POST /api/v1/terminal/terminals/status/?from_guacamole=1 HTTP/1.1"},
	{"message":"172.17.0.2 [28/Mar/2022:23:59:41 +0800] POST /api/v1/terminal/terminals/status/ HTTP/1.1"}
	]
}
'''
# print("## data:",type(data))

list='''
[
	{"message":"172.17.0.3 [28/Mar/2022:23:59:19 +0800] POST /api/v1/terminal/terminals/status/?from_guacamole=1 HTTP/1.1"},
	{"message":"172.17.0.2 [28/Mar/2022:23:59:21 +0800] POST /api/v1/terminal/terminals/status/ HTTP/1.1"},
	{"message":"172.17.0.3 [28/Mar/2022:23:59:29 +0800] POST /api/v1/terminal/terminals/status/?from_guacamole=1 HTTP/1.1"},
	{"message":"172.17.0.2 [28/Mar/2022:23:59:33 +0800] GET /api/v1/terminal/terminals/config/ HTTP/1.1"},
	{"message":"172.17.0.3 [28/Mar/2022:23:59:39 +0800] POST /api/v1/terminal/terminals/status/?from_guacamole=1 HTTP/1.1"},
	{"message":"172.17.0.2 [28/Mar/2022:23:59:41 +0800] POST /api/v1/terminal/terminals/status/ HTTP/1.1"}
]
'''
# print("## list:",type(list))

ret = json.loads(list)
# print("## ret:",type(ret))

for i in ret:
	# print("## i:",type(i))
	line = i["message"]
	# print("## line:",type(line))
	if re.search('GET',line) != None:
		print(line)
