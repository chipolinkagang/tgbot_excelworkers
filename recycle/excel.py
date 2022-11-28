# на вход получает 5 работников, сформировать таблицу excel и отправить в чат.
import datetime

import xlsxwriter
from typing import List


def create5_excel(people: List[dict]):
    workbook = xlsxwriter.Workbook('demo.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('B:B', 40)
    worksheet.write(0, 0, "id")
    worksheet.write(0, 1, "fio")
    worksheet.write(0, 2, "datar")
    worksheet.write(0, 3, "id_role")

    counter = 1
    for peop in people:
        worksheet.write(counter, 0, str(peop["id"]))
        worksheet.write(counter, 1, peop["fio"])
        worksheet.write(counter, 2, peop["datar"])
        worksheet.write(counter, 3, peop["id_role"])
        counter += 1
    workbook.close()

# create5_excel({{"id": 1, "fio": "bla bla bla", "datar": datetime.datetime(2009, 1, 6), "id_role": 0},
#                {"id": 1, "fio": "bla g bla", "datar": datetime.datetime(2009, 1, 6), "id_role": 0},
#                {"id": 1, "fio": "bla d bla", "datar": datetime.datetime(2009, 1, 6), "id_role": 0},
#                })
