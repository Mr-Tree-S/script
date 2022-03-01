import requests

if __name__ == "__main__":
    url="https://www.baidu.com/"
    response=requests.get(url=url)
    page_txt=response.text
    print(page_txt)
    with open('./baidu.html','w',encoding='utf-8') as fp:
        fp.write(page_txt)
    print('end!!!')