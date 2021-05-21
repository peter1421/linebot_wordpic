import requests
from bs4 import BeautifulSoup
import os
from fake_useragent import UserAgent
import random
import re


def get_root(url):
    res = requests.get('https://free-proxy-list.net/')
    m = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)
    re200 = "[200]"
    for ip in m:
        try:
            ua = UserAgent().chrome
            response = requests.get(
                url, headers={"user-agent": ua}, proxies={'http': ip, 'https': ip}, timeout=5)
            print(response,ip)
            if(response.ok):
                print("ok")
                root = BeautifulSoup(response.text, "html.parser")
                return root
            else:
                print(response, "!=<Response [200]>")
                continue
        except:
            print('FAIL', ip)
    return 0

###
def get_txt(root):
    ans = []
    floor = root.find_all("div", class_="c-article__content")
    for x in floor:
        ans.append(x.text.strip("\n"))
    return ans



def save_txt(lis):
    file_name = os.path.dirname(__file__)+"/word.txt"
    f = open(file_name, 'w', encoding='utf8')
    f.truncate(0)
    print("寫入:", lis)
    for x in lis:
        try:
            f.write(x+" ")
        except:
            print("N\n")
    f.close()
    lis.clear()
    print(file_name, "存檔成功\n")


def all_floor(url):
    ans = []
    root = get_root(url)
    p = 1
    s = "https://forum.gamer.com.tw/C.php"
    ans.extend(get_txt(root))
    while(1):
        try:
            p += 1
            page = root.find("a", class_="next")
            url = s+page["href"]
            root = get_root(url)
            ans.extend(get_txt(root))
            print(p, "頁完成\n")
            ss=p
        except:
            print("輸出", ans)
            save_txt(ans)
            break


url = "https://forum.gamer.com.tw/Co.php?bsn=60076&sn=74427703"

all_floor(url)


# proxy_list = [
#     '24.217.192.131:57273',
#     '195.182.152.238:38178',
#     '79.143.87.117:9090',
#     '82.102.8.60:3128',
#     '24.217.192.131:57273'
#     '82.102.8.60:3128'
#     '51.81.21.221:3128'
#     '110.76.129.106:59570'
#     '123.231.244.237:8080'
# ]
# proxy = random.choice(proxy_list)
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# }, proxies=proxies
# print(proxies)
