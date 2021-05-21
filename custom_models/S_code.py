import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


class shop_data:
    def __init__(self, url):
        self.headers = {'User-Agent': 'Googlebot',
                        'From': 'abcde12345326@gmail.com'}
        self.url = url
        self.root = None
        self.content = None
        self.title = None
        self.price = None
        self.priceCurrency = None
        self.now = datetime.now().strftime('%Y-%m-%d_%H:%M')

    def get_data(self):
        response = requests.get(
            self.url, headers=self.headers, allow_redirects=True)
        self.root = BeautifulSoup(response.text, "html.parser")

    def get_content(self):
        self.content = self.root.find_all(
            'script', {'type': 'application/ld+json'})[-1].prettify()
        self.content = json.loads(self.content[50:-10])

    def get(self):
        self.get_data()
        self.get_content()

    def get_title(self):
        self.title = self.content["name"]
        return self.title

    def get_price(self):
        self.price = self.content["offers"]["price"]
        return self.price

    def get_priceCurrency(self):
        self.priceCurrency = self.content["offers"]["priceCurrency"]
        return self.priceCurrency

    def show(self):
        

        n = self.get_title()+ "=>"+self.get_price()+self.get_priceCurrency()
        #print(n)
        return n
   


def s_data(url):
    data1 = shop_data(url)
    data1.get()
    text=data1.show()
    #print(text)
    data1_list=[]
    data1_list.append(data1.title)
    data1_list.append(data1.price)

    print(data1_list[0],":",data1_list[1])
    return data1_list
#輸出商品價格與金額


# url = "https://shopee.tw/product/124885008/9610930766/"
# s_data(url)
#print(float(data1.get_price()))
