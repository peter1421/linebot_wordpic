#%%
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import re
import pandas

def get_root(url):
    try:
        try:
            response = requests.get(url,timeout=5)
            root = BeautifulSoup(response.text, "html.parser")
            return root
        except:    
            ua = UserAgent().chrome
            response = requests.get(url, headers={"user-agent": ua}, timeout=5)
            root = BeautifulSoup(response.text, "html.parser")
            return root
    except:    
        res = requests.get('https://free-proxy-list.net/')
        m = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)
        for ip in m:
            try:
                ua = UserAgent().chrome
                response = requests.get(
                    url, headers={"user-agent": ua}, proxies={'http': ip, 'https': ip}, timeout=5)
                print(response, ip)
                if(response.ok):
                    print("ok")
                    root = BeautifulSoup(response.text, "html.parser")
                    return root
                else:
                    continue
            except:
                print('FAIL', ip)
        return 0



def get_txt(root):
    ans = []
    head = 'https://tw.appledaily.com/'
    floor = root.find_all("div", class_="flex-feature")
    for x in floor:
        temp = []
        link = head+(x.find("a", class_="story-card")['href'])
        title = x.find("span", class_="headline truncate truncate--3").text
        temp = [title, link]
        ans.append(temp)
    return ans


def get_list():
    url='https://tw.appledaily.com/home/'
    root=get_root(url)
    w=get_txt(root)
    for x in w:
        print("標題:{}\n網址:{}\n\n".format(x[0],x[1]))
    return w 
 
df = pandas.DataFrame(get_list())

#%%




