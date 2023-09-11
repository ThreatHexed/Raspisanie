import json
import re
import openpyxl

# def zameni(day, group,):
    



#     excel_file = openpyxl.load_workbook('X:/123/Output.xlsx')
#     employees_sheet = excel_file['Лист1']

# with open('pari.json', 'r', encoding='utf-8') as f:
#     pari = json.load(f)



#     for p in range(0,7):
    
#         for para in pari['pari'][p][group][day]:
#             for i in para:
#                 cell = pari['pari'][p][group][day][i]['para']
#                 pari_norm['pari'][p][group][day][i]['para'] = re.sub(" +", " ", str(employees_sheet[cell].value))


# zameni()

s = "4п. – нет  5п. МДК 05.01 Рысцова, 412 ауд"


b = (s.split('п.')[1])
for i in (0,1):
    for z in (0,1):
        for x in list(re.sub(",", "", (s.split('п')[0+i]))):
            print (x + s.split('п.')[1+z])