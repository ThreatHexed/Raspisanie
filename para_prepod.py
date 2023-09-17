import pandas as pd
import json
from datetime import date
from datetime import datetime
import locale
import numpy as np



def raspisanietop2(prepod):
    
    try:
        
        weekday = ['0', "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Понедельник", "Понедельник"]
        

        if datetime.now().hour > 8:
            userdate = str(date.today().isoweekday()+1)
            
        else: 
            userdate = str(date.today().isoweekday())
            
            
        with open("1234.json", "r", encoding='utf-8') as f:
            data = json.load(f)
        

        day = data[userdate]

        

        excel = pd.read_excel(io='test1.xlsx',
                    engine='openpyxl',
                    usecols='A:S',
                    header=8,
                    )

        para = f'{weekday[int(userdate)]}\n\n'

        
        for id, day_number in enumerate(day, 2):
        
            
            for group in excel:
                


                if str(excel[group].loc[day[day_number]]).find(str(prepod))  > -1:
                    para += (f"{excel[group].loc[0]} \n {excel[group].loc[day[day_number]-1]} \n {excel[group].loc[day[day_number]]}\n____________\n")
        if prepod == 'Колесников':
            para += "\nТакого преподавателя я в хуй не дул, и вообще, дядя, кто ты нахуй такой"


           

        return para                 
    except Exception as e:
        return f"Ой, ошибочка вышла"