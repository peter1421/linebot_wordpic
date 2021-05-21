import requests
from bs4 import BeautifulSoup
import os


def get_root(url):
    response = requests.get(url, headers={
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
    root = BeautifulSoup(response.text, "html.parser")
    return root


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
    for x in lis:
        try:
            f.write(x+" ")
        except:
            print("N\n")
    f.close()
    lis.clear()
    print("存檔成功\n")


def all_floor(url):
    ans = []
    root = get_root(url)
    p = 1
    s = "https://forum.gamer.com.tw/C.php"
    ans.extend(get_txt(get_root(url)))
    while(1):
        try:
            p += 1
            page = root.find("a", class_="next")
            url = s+page["href"]
            root = get_root(url)
            ans.extend(get_txt(get_root(url)))
            print(p, "頁完成\n")
        except:
            save_txt(ans)
            break


# url = "https://forum.gamer.com.tw/C.php?bsn=60076&snA=5927878&tnum=122&bPage=2"

# all_floor(url)
