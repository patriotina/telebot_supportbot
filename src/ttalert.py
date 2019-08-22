import constants
import telebot
import datetime
import time
from telebot import types
from telebot.types import InlineKeyboardButton
#from flask import Flask

bot = telebot.TeleBot(constants.ttalarm)
t_message = ''


@bot.message_handler(commands=["start"])
def cmd_start(message):
    answer = 'Начнем'
    #log(message, answer)

    #tb_msg.is_start = True
    t_message = ''
    t_message += str(datetime.datetime.now()) + '\n'
    t_message += 'Message from {0} {1}; AKA {2} ID: {3}; From chat: {4}; \n'.format(message.from_user.first_name,
                                                            message.from_user.last_name,
                                                            message.from_user.username,
                                                            str(message.from_user.id),
                                                            message.chat.title)
    print(str(message))

    keyboard = types.InlineKeyboardMarkup()
    #url_button = types.InlineKeyboardButton(text="Перейти к списку заявок", url="http://help.373soft.ru/issues")
    #keyboard.add(url_button)
    inl_button = types.InlineKeyboardButton(text="Авария!", callback_data='AlarmOn')
    inl_button2 = types.InlineKeyboardButton(text="Проблема решена", callback_data='AlarmOff')
    iss_but = types.InlineKeyboardButton(text='Создать заявку', url="help.373soft.ru/create_task/")
    keyboard.row(inl_button, inl_button2, iss_but)
    #keyboard.add(inl_button)
    #keyboard.add(inl_button2)
    #bot.send_message(message.from_user.id, "Что у нас?", reply_markup=keyboard)

    #keyboard = types.ReplyKeyboardMarkup(True, False)
    #keyboard.row('/alarm', '/ok')

    ans = bot.send_message(message.chat.id, 'Всё ок?', reply_markup=keyboard)


@bot.message_handler(commands=["alarm"])
def cmd_alarm(message):
    alm_message = 'Alarm;'
    alm_message += str(datetime.datetime.now()) + ';'
    alm_message += str(message.from_user.id) + ';'
    alm_message += str(message.chat.id)
    print(alm_message)
    keyboard = types.InlineKeyboardMarkup()
    # url_button = types.InlineKeyboardButton(text="Перейти к списку заявок", url="http://help.373soft.ru/issues")
    # keyboard.add(url_button)
    inl_button = types.InlineKeyboardButton(text="Подать заявку", url="help.373soft.ru/create_task/")
    inl_button2 = types.InlineKeyboardButton(text="Посмотреть заявки", url="help.373soft.ru/issues/")
    keyboard.row(inl_button, inl_button2)
    ms = bot.send_message(message.chat.id, alm_message, reply_markup=keyboard)
    alm_message = ''


@bot.message_handler(commands=["ok"])
def cmd_norm(message):
    alm_message = 'AlarmOff;'
    alm_message += str(datetime.datetime.now()) + ';'
    alm_message += str(message.from_user.id) + ';'
    alm_message += str(message.chat.id)
    print(alm_message)
    ms = bot.send_message(message.chat.id, alm_message)


@bot.inline_handler(func=lambda query: len(query.query) is 0)
def empty_query(query):
    hint = "первый хинт"
    try:
        r = types.InlineQueryResultArticle(
                id='1',
                #parse_mode='Markdown',
                title="Бот \"Спасатель\"",
                description=hint,
                input_message_content=types.InputTextMessageContent(
                    message_text="Подать заявку на Аварию"),
                url="http://help.373soft.ru/create_task",
                #disable_web_page_preview=True,
                # Не будем показывать URL в подсказке
                hide_url=False
        )

        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)


restricted_messages = ['Авария', 'авария', 'авари', 'Авари']
GROUP_ID = -367377146
ro_msg = 'Вам запрещено отправлять сюда сообщения в течение 10 минут'
city_list = {'test': -367377146}
city_alarm_list = {}

#@bot.message_handler(func=lambda message: message.text and message.text.lower() in restricted_messages)# and message.chat.id == GROUP_ID)
@bot.message_handler(content_types='text')
def find_alarm(message):
    #print(message)
    if 'авария' in message.text.lower():

        #print(alm_message)
        reply_keyboard = types.InlineKeyboardMarkup()
        #alarm_url = 'help.373soft.ru/alarm?alrm_msg_id=' + str(message.message_id) + '&alrm_author=' + str(message.from_user.id) + '&alrm_city=' + str(message.chat.id)
        #inl_button = types.InlineKeyboardButton(text="Да", url=alarm_url)
        inl_button2 = types.InlineKeyboardButton(text="Нет", callback_data='AlarmOff')
        #iss_but = types.InlineKeyboardButton(text='Создать заявку', url="help.373soft.ru/create_task/")
        #reply_keyboard.row(inl_button, inl_button2)

        ms = bot.send_message(message.chat.id, 'Случилась авария? ')

        alarm_url = 'help.373soft.ru/alarm?alrm_msg_id=' + str(ms.message_id) + '&alrm_author=' + str(message.from_user.id) + '&alrm_city=' + str(message.chat.id)
        inl_button = types.InlineKeyboardButton(text="Да", url=alarm_url)
        reply_keyboard.row(inl_button, inl_button2)
        bot.edit_message_text(text='Случилась авария?', chat_id=ms.chat.id, message_id=ms.message_id, reply_markup=reply_keyboard)
        #bot.send_message(message.chat.id, ms.message_id)
        #bot.delete_message(message.chat.id, 261)
        #print(message.text)
        #print(message.chat.id)
        #bot.edit_message_text(text='хуярия', chat_id=message.chat.id, message_id=331)



@bot.callback_query_handler(func=lambda c: True)
def calls(c):

    if c.data == 'AlarmOn':
        alm_message = 'AlarmOn;'
        city_alarm_list[c.message.chat.id] = 1
        reply_keyboard = types.InlineKeyboardMarkup()
        inl_button = types.InlineKeyboardButton(text="Исправлено", url='ya.ru')
        reply_keyboard.row(inl_button)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Взято в работу', reply_markup=reply_keyboard)

    elif c.data == 'AlarmOff':
        alm_message = 'AlarmOff;'
        city_alarm_list[c.message.chat.id] = 0
        bot.delete_message(c.message.chat.id, c.message.message_id)

    alm_message += str(datetime.datetime.now()) + ';'
    alm_message += str(c.message.from_user.id) + ';'
    alm_message += str(c.message.chat.id)
    alm_message += str('\n')
    f = open('alarm.log', 'a')
    f.write(alm_message)
    f.close()
    #bot.send_message(c.message.chat.id, alm_message)


    # Банить будем за капслок, постепенно
    # print('Yyyeeeaaahh')
    # bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time()+6)
    # bot.send_message(message.chat.id, ro_msg,
    #             reply_to_message_id=message.message_id)


if __name__ == '__main__':
    try:
        bot.polling(none_stop = True)
    except Exception:
        time.sleep(15)
