import pandas as pd
import json
from datetime import date
from datetime import datetime

import numpy as np



def raspisanietop2(prepod):
    
    # try:
        day228 = ['0', "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        

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

        para = ""
        print(day)
        for day1337 in day:

            for group in text:
            
                superday = int(day[day1337])
                if str(text[group].loc[superday]).find(str(prepod))  > -1 :
                    para += (f"{text[group].loc[superday-1]} \n {text[group].loc[superday]}")
                

    #     return para                 
    # except:
    #     return "ошибка"
    
