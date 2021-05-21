#import forum_fun as f, get_pic as g
from fun import forum_fun as f, get_pic as g
import numpy as np
import matplotlib.pyplot as plt
import pyimgur


def glucose_graph(url):
    f.all_floor(url)
    g.get_img()
    CLIENT_ID = "cb4c8860e31c56a"
    PATH = "Wordcloud.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    print("圖片網址:",uploaded_image.link)
    return uploaded_image.link


# url = "https://forum.gamer.com.tw/C.php?bsn=60076&snA=6344509"
# img_url = glucose_graph(url)
# print(img_url)




