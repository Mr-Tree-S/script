import requests
import json
if __name__ == "__main__":
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    
    id_list = []
    for page in range(0,1):
        data={
            'on':'true',
            'page':page,
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
            'applysn':'',
        }
        json_ids=requests.post(url=url,headers=headers,data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    # com detail
    post_url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        data={
            'id':id
        }
        detail_json=requests.post(url=post_url,headers=headers,data=data).json()
        print(detail_json['epsName'])
    print('########END#########')