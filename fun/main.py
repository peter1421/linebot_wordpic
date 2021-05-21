#import forum_fun as f, get_pic as g,database as da
from fun import forum_fun as f, get_pic as g,database as da
import numpy as np
import matplotlib.pyplot as plt
import pyimgur


def glucose_graph(id_t,url):
    f.all_floor(url)
    g.get_img()
    CLIENT_ID = "cb4c8860e31c56a"
    PATH = "Wordcloud.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    da.save_url(id_t, uploaded_image.link)
    return uploaded_image.link


def find_pic(id_t):
    d = da.database(id_t, url=None)
    if(d.check_re_id):
        ls = d.select()
        for x in range(len(ls)-1, 0, -1):
            if(ls[x][1] == id_t):
                print(ls[x][2])
                return ls[x][2]
    return "NULL"


#find_pic("U3710ef56fd850e8a225091b26a67daea")

# url = "https://forum.gamer.com.tw/C.php?bsn=60076&snA=6344509"
# img_url = glucose_graph("N", url)
#print(img_url)




