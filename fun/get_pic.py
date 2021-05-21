from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import jieba
import numpy as np
from collections import Counter
import os
def get_img():
    file_name = os.path.dirname(__file__)+"/word.txt"

    text_from_file_with_apath = open(file_name, "r", encoding="utf-8").read()

    print(file_name,"讀取完成")

    print("內文:",text_from_file_with_apath)
    # 設定字典
    dict_name = os.path.dirname(__file__)+"/dict.txt.big"
    userdict_name = os.path.dirname(__file__)+"/userdict.txt"

    jieba.set_dictionary(dict_name)
    jieba.load_userdict(userdict_name)

    # 設定停用詞，譬如唱歌會用到的oh，喔
    stopWord = os.path.dirname(__file__)+"/stopWord.txt"

    with open(stopWord, 'r', encoding='utf8') as f:
        stops = f.read().split('\n')

    #
    # 開始段詞與排序，沒錯就這麼簡單就做完了
    #
    terms = [t for t in jieba.cut(text_from_file_with_apath,cut_all=True)if t not in stops and len(t) > 1]

    sorted(Counter(terms).items(), key=lambda x: x[1], reverse=True)

    print("??", Counter(terms), "??")
    print("!!", terms, "!!")

    # 中文繪圖需要中文字體，請自己從windows font目錄抓
    # 微軟正黑體
    font = os.path.dirname(__file__)+"/msjh.ttc"
    png_n = os.path.dirname(__file__)+"/okpng.png"

    # 想要文字雲出現的圖示
    mask = np.array(Image.open(png_n))


    my_wordcloud = WordCloud(background_color="black", mask=mask, collocations=False, width=2400, height=2400, margin=2)
    my_wordcloud.generate_from_frequencies(Counter(terms))

    # 產生圖片
    plt.figure(figsize=(20, 10), facecolor='k')
    plt.imshow(my_wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    # 顯示用
    #plt.show()

    # 存檔用
    plt.savefig("Wordcloud.png")


# url = "https://forum.gamer.com.tw/C.php?bsn=60076&snA=6344509"
# forum_fun.all_floor(url)
#get_img()
