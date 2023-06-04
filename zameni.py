import json
import re
import openpyxl

def zameni(day, group,):
    

# ///
# Алллах защити мой код
# ///


    excel_file = openpyxl.load_workbook('X:/123/Output.xlsx')
    employees_sheet = excel_file['Лист1']

with open('pari.json', 'r', encoding='utf-8') as f:
    pari = json.load(f)



    for p in range(0,7):
    
        for para in pari['pari'][p][group][day]:
            for i in para:
                cell = pari['pari'][p][group][day][i]['para']
                pari_norm['pari'][p][group][day][i]['para'] = re.sub(" +", " ", str(employees_sheet[cell].value))


zameni()