import pandas as pd
import json
from datetime import date
from datetime import datetime


def raspisanietop(group):

    try:
        day228 = ['0', "Понедельник", "Вторник", "Среда", "Четверг",
                  "Пятница", "Суббота", "Понедельник", "Понедельник"]

        if datetime.now().hour > 12:
            date1 = str(date.today().isoweekday()+1)
            date2 = int(date.today().isoweekday()+1)
        else:
            date1 = str(date.today().isoweekday())
            date2 = int(date.today().isoweekday())
        with open("123.json", "r", encoding='utf-8') as f:
            data = json.load(f)

        raspisanie = f'{day228[date2]}\n'

        day = data[date1]

        text = pd.read_excel(io='test1.xlsx',
                             engine='openpyxl',
                             usecols='A:S',
                             header=9,
                             )

        text = text.fillna("Сиди играй в дотку")

        for id, i in enumerate(day, 2):

            day1 = int(day[i])
            if id % 2 == 0:
                id -= int(id/2)
            else:
                id = ""
            raspisanie += f'\n{str(id)} {str(text[group].loc[day1])}'

        return raspisanie
    except Exception as e:
        return f"Ошибки \n {e} \n А теперь пиздуй чинить"
