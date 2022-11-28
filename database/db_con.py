# запись работника в таблицу users(ФИО, рандом др, роль(рандом из таблицы roles)
# вывод последних добавленных 5 работников
import datetime
import json
import random
from random import randrange
from typing import List

import sqlalchemy as sa
import sqlite3
from sqlalchemy import insert
from sqlalchemy import Table, MetaData
from sqlalchemy import create_engine

metadata = sa.MetaData()

roles = sa.Table('roles', metadata,
                 sa.Column('id', sa.Integer, primary_key=True),
                 sa.Column('name', sa.String(50)))

users = sa.Table('users', metadata,
                 sa.Column('id', sa.BIGINT, primary_key=True),
                 sa.Column('fio', sa.String(255)),
                 sa.Column('datar', sa.String(255)),
                 sa.Column('id_role', sa.Integer))

with open("C:\\Users\\kiril\\PycharmProjects\\testbotjob_project\\config.json", 'r',
          encoding='utf-8') as f:  # открыли файл
    options = json.load(f)  # загнали все из файла в переменную

db = options["data_base"]  # путь к бд


def next_id(table: str) -> int:
    conn = sqlite3.connect(db)
    cursorn = conn.cursor()
    cursorn.execute("SELECT Count(*) FROM " + table)
    x = cursorn.fetchall()[0][0] + 1
    conn.close()
    return x


def random_date(start):
    end = datetime.datetime.now() - 16 * datetime.timedelta(days=365)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def insert_table(inp_fio: str) -> bool:
    try:
        nid = next_id("users")
        stmt = insert(users).values(id=nid, fio=inp_fio, datar=random_date(datetime.datetime(1970, 5, 1)),
                                    id_role=random.randint(1, 2))
        engine = create_engine("sqlite:///C:\\Users\\kiril\\PycharmProjects\\testbotjob_project\\database\\database.db", echo=True, future=True)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
            return True
    except:
        return False


# print(insert_table("Ivanova Daria Olegovna"))


def get_5last_users() -> List[dict]:
    con = sqlite3.connect(db)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 5")

    ar = []
    for us in cursor.fetchall():
        ar.append({"id": us[0], "fio": us[1], "datar": us[2], "id_role": us[3]})
    con.close()
    return ar

# print(get_5last_users())

# with con:
#     con.execute("""
#             CREATE TABLE roles (
#                 id INT PRIMARY KEY,
#                 name VARCHAR(50)
#             );
#         """)
#     con.execute("""
#         CREATE TABLE users (
#             id BIGINT PRIMARY KEY,
#             fio VARCHAR(30),
#             datar DATE,
#             id_role INT,
#             FOREIGN KEY (id_role) REFERENCES roles (id)
#         );
#     """)
