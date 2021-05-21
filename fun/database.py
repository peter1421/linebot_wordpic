import os
import psycopg2


class database():
    def __init__(self, id_t, url):
        self.DATABASE_URL = os.environ['DATABASE_URL']
        #self.DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a dsfsfsfssf').read()[:-1]
        self.conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
        self.id = id_t
        self.url = url

    def creat_table(self):
        create_table_query = '''CREATE TABLE ID_table(
                record_no serial PRIMARY KEY,
                ID VARCHAR (500) NOT NULL,
                url VARCHAR (500) NOT NULL
                );'''
        self.close(create_table_query)
        print("列表已建立")

    def delete_table(self):
        delete_table_query = '''DROP TABLE IF EXISTS ID_table'''
        self.close(delete_table_query)
        print("列表已刪除")

    def add_table(self):
        cursor = self.conn.cursor()
        record = (self.id, self.url)
        table_columns = '(ID, url)'
        postgres_insert_query = f"""INSERT INTO ID_table {table_columns} VALUES (%s,%s);"""
        cursor.execute(postgres_insert_query, record)
        self.conn.commit()
        count = cursor.rowcount
        print(count, "筆資料添加完成")
        cursor.close()

    def del_line(self, num):
        cursor = self.conn.cursor()
        del_num = f"""DELETE from ID_table WHERE record_no = {str(num)}"""
        print("!!!", del_num)
        cursor.execute(del_num)
        self.conn.commit()
        print("資料刪除完成")
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
                print(y, end=":")
            print("\n")

    def check_re_id(self):
        ls = self.select()
        for x in ls:
            if(self.id == x[1]):
                return True
        return False


def save_url(id_t, url):
    d = database(id_t, url)
    d.add_table()
    d.show_table()
#d = database("bb","fff")
# d.creat_table()
# d.add_table()
# d.show_table()


def show_new():
    try:
        d = database(id_t='dd', url='dd')
        # d.add_table()
        ls = d.select()
        temp = ls[-1]
        d.del_line(temp[0])
        print(temp)
        return temp
    except:
        return None

# show_new()

# d = database("bb","fff")
# d.add_table()

# # d = database("bb", "fff")
# d.show_table()


# find_pic("U3710ef56fd850e8a225091b26a67daea")
# save_url("ss","s")
#d = database("5", url=None , lis=None)
# d.creat_table()
# d.add_table()
# d.show_table()
# d.delete_table()

# 用不到
def show_id():
    d = database("0", url=None, lis=None)
    ls = d.select()
    arr_ls = []
    for x in ls:
        if(x[1] == "o"):
            continue
        arr_ls.append(x[1])
        # print(x[1])
    return arr_ls


def save_id(id_t):
    try:
        d = database(id_t, url=None, lis=None)
        if(d.check_re_id() == False):
            d.add_table()
            d.show_table()
            t = "id"+"儲存完成"
        else:
            t = "id:("+str(id_t)+")已存在"
        return t
    except:
        return None
