import requests
import re

if __name__ == "__main__":
	headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
		}
	
	for page in range(1, 2):
		data = {
			'page': page,
		}
		url = 'https://www.seebug.org/vuldb/vulnerabilities?page='+str(page)
		vul = requests.get(url=url, headers=headers).text
		# print(vul)
		with open('./vul.html', 'w', encoding='utf-8') as fp:
			fp.write(vul)
		
		# reg = re.findall(r'title(.+?)vuldb/(.+?)">(.+?)</a></td>',vul)
		reg = re.findall(r'<a class="vul-title" title=(.+?) href=',vul)

		for i in reg:
			print(i)
	print('################  END  #################')