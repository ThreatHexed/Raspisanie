from datetime import datetime
import telebot
from telebot import types
from data import token
import random
import raspisanie
import locale
import anekdot


locale.setlocale(locale.LC_ALL, "ru")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Случайный анекдот")
    btn2 = types.KeyboardButton(f"🕑Замены")
    markup.add(btn1, btn2)
    dt = datetime.today().strftime("%A, %d.%m.%Y")
    day_part = int(datetime.today().hour)


    if day_part > 0 and  day_part < 6:
        if random.randint(1, 100) == 100:
            text2 = ("Хуле палишь, ты время видел?\nИди в доту, гений")
        else:
            text2 = ("Хуле палишь, ты время видел?\nИди в кроватку, пупсик <3")

    elif day_part > 6 and  day_part < 12:
        text2 = ("Доброе утро!")

    elif day_part > 12 and  day_part < 16:
        text2 = ('Добрый день!')

    elif  day_part > 16 and  day_part < 23.59:
        text2 = ('Добрый вечер!')


    text = f"{text2}\n\nСегодня: {dt}\n"
    bot.send_message(message.chat.id, text=text.format(
        message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Случайный анекдот"):
        bot.send_message(message.chat.id, text=anekdot.get_first_news())
    


    elif(message.text == "🕑Замены"):
        msg = bot.send_message(message.chat.id, text="Напишите номер группы")
        bot.register_next_step_handler(msg, get_group)
        
        
        
    elif (message.text == "Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Случайный анекдот")
            btn2 = types.KeyboardButton(f"🕑Замены")
            markup.add(btn1, btn2)
            dt = datetime.today().strftime("%A, %d.%m.%Y")
            day_part = int(datetime.today().hour)


            if day_part > 0 and  day_part < 6:
                if random.randint(1, 100) == 100:
                    text2 = ("Хуле палишь, ты время видел?\nИди в доту, гений")
                else:
                    text2 = ("Хуле палишь, ты время видел?\nИди в кроватку, пупсик <3")

            elif day_part > 6 and  day_part < 12:
                text2 = ("Доброе утро!")

            elif day_part > 12 and  day_part < 16:
                text2 = ('Добрый день!')

            elif  day_part > 16 and  day_part < 23.59:
                text2 = ('Добрый вечер!')


            text = f"{text2}\n\nСегодня: {dt}\n"
            bot.send_message(message.chat.id, text=text.format(
                message.from_user), reply_markup=markup)
            # bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..\nНапиши /start")



@bot.message_handler(content_types=['text'])
def get_group(message):
    group = (message.text).upper()
    if raspisanie.get_table(group) != False:
        
        back = types.KeyboardButton("Вернуться в главное меню")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(back)
        bot.send_message(message.chat.id, text=raspisanie.get_table(group), reply_markup=markup)

    elif raspisanie.get_table(group) == False:
        back = types.KeyboardButton("Вернуться в главное меню")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(back)
        bot.send_message(message.chat.id, text=f'Для группы {group} замен не найдено', reply_markup=markup)

    # huyna(message, group)

@bot.message_handler(content_types=['text'])
def huyna(message):
    bot.send_message(message.chat.id, text='Ищу замены🧐')


# @bot.message_handler(content_types=['text'])\
# def group_choose(message):
    
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
