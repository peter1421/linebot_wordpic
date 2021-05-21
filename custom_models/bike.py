import json
import ssl
import urllib.request
def get_data():
    url = 'https://datacenter.taichung.gov.tw/swagger/OpenData/34c2aa94-7924-40cc-96aa-b8d090f0ab69'
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8-sig'))
    return data
def show_data(data):
    for i in data['retVal']:
        print(data['retVal'][i]['sno'], '\t')
        print(data['retVal'][i]['sna'], '\n')
def show_bike(data, num):
    try:
        print(data['retVal'][num]['sna'], "的剩餘車位:", data['retVal'][num]['sbi'])
    except:
        print(num, "錯誤,請輸入正確編號", '\n')
def re_show_data(data):
    re=""
    for i in data['retVal']:
        re += data['retVal'][i]['sno']+str('\t')+data['retVal'][i]['sna']+ str('\n')
    return re
def re_show_bike(data, num):
    re=""
    try:
        re = data['retVal'][num]['sna']+ "的剩餘車位:"+data['retVal'][num]['sbi']
    except:
        re = str(num)+"錯誤,請輸入正確編號"
    return re