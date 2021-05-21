import requests
import bs4
import random

def get(url):
    response = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
    root = bs4.BeautifulSoup(response.text, "html.parser")
    print(response)
    return root


def get_news(root):
    title = root.find_all('h3')
    c = 0
    n = 'https://news.google.com'
    l = []
    for x in title:
        c += 1
        u = x.find('a', class_="DY5T1d RZIKme")
        u = n+u['href'][1:]
        # print(x.text)
        l.append(x.text)
        l.append(u)
        if(c > 2):
            break
    return l


#lis = get_news(get(url))
def new_data():
    url = 'https://news.google.com/search?q=%E9%9F%93%E5%9C%8B%E7%91%9C&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
    lis = get_news(get(url))
    r = random.randint(0, int(len(lis)/2)-1)
    w = lis[2*r]+"\n"+lis[2*r+1]
    return w
#new_data()
