import requests
import pandas as pd
import time

datas = pd.DataFrame()
url = 'https://www.lagou.com/jobs/positionAjax.json?'
headers = {
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=sug&fromSearch=true&suginput=%E6%95%B0%E6%8D%AE',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie':'user_trace_token=20180525154449-80e8cc86-5fef-11e8-9b2b-525400f775ce; LGUID=20180525154449-80e8d0b7-5fef-11e8-9b2b-525400f775ce; LG_LOGIN_USER_ID=a8165d1ead5fd7432445334d6eee0610fb7d417e3f7fcc44632d0a5f9d70bf20; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216396b1e3e1198-0062aac7dc48a3-151b7557-1049088-16396b1e3e21b2%22%2C%22%24device_id%22%3A%2216396b1e3e1198-0062aac7dc48a3-151b7557-1049088-16396b1e3e21b2%22%7D; JSESSIONID=ABAAABAAAFCAAEGDE29BB671DB34FC64703CB7594997D93; _putrc=CDF07A50CE0601FC123F89F2B170EADC; login=true; unick=%E9%BE%9A%E5%AD%A6%E9%9B%B7; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=62; gate_login_token=a3ed4d08b87a29f0358e9db3134456c6110e9e7c2ee119721b461a7c055f1853; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; _gid=GA1.2.1534874378.1527471044; _ga=GA1.2.1893973794.1527234268; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1527558289,1527660975,1527730510,1527834620; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1527920554; LGSID=20180602141722-9c51339e-662c-11e8-935c-5254005c3644; LGRID=20180602142252-612246cb-662d-11e8-935c-5254005c3644; TG-TRACK-CODE=search_code; SEARCH_ID=5e5da69a981f4b02b7f4b687ce6edafe; index_location_city=%E4%B8%8A%E6%B5%B7',
        }
for i in range(1,31):
    params = {
        'city': '上海',
        'needAddtionalResult': 'false',
        'first': 'true',
        'pn': i,
        'kd': '数据分析',
        }

    web_data = requests.get(url,params=params,headers=headers)
    data_json = web_data.json()
    result = data_json['content']['positionResult']['result']
    data = pd.DataFrame(result)
    datas = pd.concat([datas,data])
    time.sleep(3)

    print(datas.shape)

datas['company_link'] = 'https://www.lagou.com/gongsi/' + datas['companyId'].astype(str) + '.html'
datas['position_link'] = 'https://www.lagou.com/jobs/' + datas['positionId'].astype(str) + '.html'

writer = pd.ExcelWriter(r'C:\Users\xuelei\Desktop/拉钩_上海_数据分析.xlsx')
datas.to_excel(writer,'Sheet1')
writer.save()