import requests as rq
import json
from datetime import date, timedelta

file_path = './data.json'


yesterday = date.today() - timedelta(days=1)
# start_date = date(2022, 11, 25)
start_date = date(2022, 11, 25)
target_date = date(2023, 6, 17)

key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJYLUFwcC1SYXRlLUxpbWl0IjoiNTAwOjEwIiwiYWNjb3VudF9pZCI6IjczODYyMDg0MSIsImF1dGhfaWQiOiIyIiwiZXhwIjoxNjk2MjIwNDIyLCJpYXQiOjE2ODA2Njg0MjIsIm5iZiI6MTY4MDY2ODQyMiwic2VydmljZV9pZCI6IjQzMDAxMTM5NyIsInRva2VuX3R5cGUiOiJBY2Nlc3NUb2tlbiJ9.a1uzzGmjXdZztvwydTrjihQpyoYG9Saa10hTEBbKESs'

cube_used = []

def start(c, d, cs) :
    url = 'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results?count='+str(c)+'&date='+str(d)+'&cursor='+cs
    res = rq.get(url, headers={'Authorization':key})
    res_js = res.json() if res and res.status_code == 200 else print('Error:', res.status_code, ', msg : ', res.text)
    return res_js

def iter():
    count = 1000
    cursor = ''
    date = start_date
    ans = []
    
    while date <= target_date:
        data = start(count, date, cursor)
        cube_log = data['cube_histories']
        cube_used.append(cube_log) if len(cube_log) != 0 else None
        date = date + timedelta(days=1)        
    

bar = '----------------------------------------------------------------------------------------------------'        

iter()
print(target_date - start_date)
#print(bar)


with open(file_path, 'w') as output:
    json.dump(cube_used, output, indent=4)