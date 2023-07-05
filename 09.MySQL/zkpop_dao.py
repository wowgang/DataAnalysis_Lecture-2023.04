# World database의 song , girl_group를 엑세스하는 라이브러리
# Connection Pool 사용
# 설치: pip install mysql-connector-python
import json
from mysql.connector import pooling

with open('./mysql.json') as f:
    config_str = f.read()
config = json.loads(config_str)
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)

def get_song_list_by_debut(year):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = ""
    cur.execute(sql, (year,))
    cur.close()
    conn.close()


def get_song_list(num, offset=0):
    conn = pool.get_connection()
    cur = conn.cursor()
    # sql = "SELECT * FROM song WHERE sid=%s;"
    sql = "SELECT * FROM song LIMIT %s OFFSET %s;"
    cur.execute(sql, (num, offset))
    cur.close()
    conn.close()
    

def get_girl_group_list(num):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM girl_group WHERE gid=%s;"
    cur.execute(sql, (num,))
    cur.close()
    conn.close()


def insert_song(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = ""
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def insert_girl_group(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql =""
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
