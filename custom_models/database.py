import os
import psycopg2
from datetime import datetime


class database():
    def __init__(self, id_t,url,lis):
        self.DATABASE_URL = os.environ['DATABASE_URL']
        #self.DATABASE_URL = os.popen(
             #'heroku config:get DATABASE_URL -a fish-talk').read()[:-1]
        self.conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        self.id = id_t
        self.url=url
        self.lis = lis
        try:
            self.S_name=self.lis[0]
            self.S_mon=self.lis[1]
        except:
            self.S_name =None
            self.S_mon = None
    def creat_table(self):
        create_table_query = '''CREATE TABLE ID_table(
                record_no serial PRIMARY KEY,
                ID VARCHAR (50) NOT NULL,
                remind VARCHAR (50) NOT NULL,
                shooping_url VARCHAR (50),
                shooping_name VARCHAR (50),
                shooping_money VARCHAR (50),
                date DATE NOT NULL,
                time TIME NOT NULL
                );'''
        self.close(create_table_query)
        print("列表已建立")

    def delete_table(self):
        delete_table_query = '''DROP TABLE IF EXISTS ID_table'''
        self.close(delete_table_query)
        print("列表已刪除")

    def add_table(self):
        cursor = self.conn.cursor()
        record = (self.id, "T", datetime.now().strftime(
            "%Y-%m-%d"), datetime.now().strftime("%I:%M:%S %p"))
        table_columns = '(ID, remind,date, time)'
        postgres_insert_query = f"""INSERT INTO ID_table {table_columns} VALUES (%s,%s,%s,%s);"""
        cursor.execute(postgres_insert_query, record)
        self.conn.commit()
        count = cursor.rowcount
        print(count, "筆資料添加完成")
        cursor.close()

    def add_shop(self):
        cursor = self.conn.cursor()
        record = (self.id, "T", datetime.now().strftime(
            "%Y-%m-%d"), datetime.now().strftime("%I:%M:%S %p"),self.url,self.S_name,self.S_mon)
        table_columns = '(ID, remind,date, time,,shooping_url,shooping_name,shooping_money)'
        postgres_insert_query = f"""INSERT INTO ID_table {table_columns} VALUES (%s,%s,%s,%s,%s,%s,%s);"""
        cursor.execute(postgres_insert_query, record)
        self.conn.commit()
        count = cursor.rowcount
        print(self.S_name+ "添加完成")
        cursor.close()

    def select(self):
        cursor = self.conn.cursor()
        postgres_select_query = f"""SELECT * FROM ID_table"""
        cursor.execute(postgres_select_query)
        data_list = cursor.fetchall()
        return data_list

    def close(self, do):
        self.conn.cursor().execute(do)
        self.conn.commit()

    def show_table(self):
        ls = self.select()
        for x in ls:
            for y in x:
                print(y)

    def check_re_id(self):
        ls = self.select()
        for x in ls:
            if(self.id == x[1]):
                return True
        return False


#d = database("5", url=None , lis=None)
#d.creat_table()
#d.add_table()
# d.show_table()
#d.delete_table()
def show_id():
    d = database("0", url=None, lis=None)
    ls=d.select()
    arr_ls=[]
    for x in ls:
        if(x[1] == "o"):
            continue
        arr_ls.append(x[1])
        ##print(x[1])
    return arr_ls


def save_shop(id_t, url, lis):
    d = database(id_t, url, lis)
    d.add_shop()

def save_id(id_t):
    d = database(id_t,url=None,lis=None)
    if(d.check_re_id() == False):
        d.add_table()
        d.show_table()
        t = "id"+"儲存完成"
    else:
        t = "id:("+str(id_t)+")已存在"
    return t
