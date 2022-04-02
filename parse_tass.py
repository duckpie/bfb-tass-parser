import time
import csv
import os
import json

import requests

base_url = 'https://tass.ru/userApi/search'

headers = {"Content-Length": "<calculated when request is sent>",
           'Host': '<calculated when request is sent>',
           'Accept': '*/*',
           'Cookie': '__js_p_=883,1800,0,0; tass_uuid=89154DC0-6ACA-4D5F-AC12-8B41CFD6E340',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.47',
           'content-type': 'application/json;charset=UTF-8',
           'cookie': "top100_id=t1.2706484.830035645.1648910914396; last_visit=1648900114402::1648910914402; t1_sid_2706484=s1.1783824344.1648910914397.1648910919035.1.5.5; SLG_G_WPT_TO=ru; __js_p_=503,1800,0,0; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; __jhash_=816; __jua_=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F99.0.4844.84%20Safari%2F537.36%20OPR%2F85.0.4341.47; __hash_=3efb822c3d5c0200c57a4ee13804055e; __lhash_=02c65abce273291181765a9f84ff06df; tass_uuid=B755FABC-FEB4-4176-BB2D-36BD32030B58; _ym_uid=1648910914415645649; _ym_d=1648910914; adtech_uid=0fcd9855-7dac-43af-86fe-21a2dbc5c2e6%3Atass.ru; user-id_1.0.5_lr_lruid=pQ8AAEJiSGK0kXV7ARSlFQA%3D; _ym_isad=2; _ym_visorc=b; top100_id=t1.2706484.1252604500.1648910920335; last_visit=1648900140119::1648910940119; t1_sid_2706484=s1.802021452.1648910920337.1648910950132.1.8.8",

           }


headers = {
'authority':'tass.ru',
'sec-ch-ua':'Not A;Brand";v="99", "Chromium";v="99", "Opera";v="85',
'accept':"application/json, text/plain, */*",
'content-type':'application/json;charset=UTF-8',
'sec-ch-ua-mobile':'?0',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.47',
'sec-ch-ua-platform':'Linux',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://tass.ru/search',
'accept-language':'ru,en-US;q=0.9,en;q=0.8',
'cookie':'top100_id=t1.2706484.830035645.1648910914396; last_visit=1648900114402::1648910914402; t1_sid_2706484=s1.1783824344.1648910914397.1648910919035.1.5.5; SLG_G_WPT_TO=ru; __js_p_=503,1800,0,0; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; __jhash_=816; __jua_=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F99.0.4844.84%20Safari%2F537.36%20OPR%2F85.0.4341.47; __hash_=3efb822c3d5c0200c57a4ee13804055e; __lhash_=02c65abce273291181765a9f84ff06df; tass_uuid=B755FABC-FEB4-4176-BB2D-36BD32030B58; _ym_uid=1648910914415645649; _ym_d=1648910914; adtech_uid=0fcd9855-7dac-43af-86fe-21a2dbc5c2e6%3Atass.ru; user-id_1.0.5_lr_lruid=pQ8AAEJiSGK0kXV7ARSlFQA%3D; _ym_isad=2; _ym_visorc=b; top100_id=t1.2706484.1252604500.1648910920335; last_visit=1648900140119::1648910940119; t1_sid_2706484=s1.802021452.1648910920337.1648910950132.1.8.8',

}

data = {"type": [],
        "sections": [],
        "searchStr": "санкции",
        "sort": "date",
        "from": 0,
        "size": 20}

response = requests.post(base_url, headers=headers, data=data)
print(response)

results = json.loads(response.text.encode())
if response.status_code == 200:
    print('Done')
else:
    print(results)
    print('ERROR: API call failed.')
