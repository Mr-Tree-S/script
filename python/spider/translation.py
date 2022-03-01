import requests
import json

if __name__ == "__main__":
    url='https://fanyi.baidu.com/sug'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

    # word=input('enter a word:')
    word=input('English:')
    data={'kw':word}

    response=requests.post(url=url,data=data,headers=headers)
    dic=response.json()
    print(dic)