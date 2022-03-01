import requests
import json

if __name__ == "__main__":
	url = 'http://192.168.0.23:8888/IDWTT'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
	}
	
	# for page in range(0, 1):
	data = {
		'command': 'ls', 	# 页码的参数名称，默认：page
	}
	r = requests.get(url=url, headers=headers, data=data).text
	
	print(r)
	print('########END#########')