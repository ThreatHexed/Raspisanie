import json

# list = ['3п', '4п', '5п', '6п']
# str = '6п соси'
# print(str.split('п')[0])





def pars(str, zamena):
    a = ('')
    list = ['понедельник', 'вторник', 'среда', 'четверг', 'пяятница', 'суббота']
  
    for i in list:
        if i in str:
            day=i
    zpara = int(zamena.split('п')[0]) 
    with open('X:/123/Raspisanie/123.json', 'r', encoding='utf-8') as f: 
        text = json.load(f) 


    for txt in text['raspisanie']: 
        if txt['day'] == day and txt['lesson'] != None and zpara != txt['pair']: 
            a+= (f"{txt['pair']} : {txt['lesson']} : {txt['teacher']}\n")
            
    a+= zamena        
    

    vse = (f'Расписание для группы ИС-213 на {day}:\n {a}')
    return vse
