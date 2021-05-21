import random
import os


def fish_talk():
    file_name = os.path.dirname(__file__)+"/talk.txt"
    print("now in ",file_name)
    f = open(file_name,
             'r', encoding='utf8')
    text = []
    for line in f.readlines():
        text.append(line)
    f.close()
    num = int(random.randint(0, len(text)))
    print(text[num])
    return text[num]


