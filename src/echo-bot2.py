# -*- coding: utf-8 -*-
import constants
import telebot
import datetime
import time
from telebot import types


bot = telebot.TeleBot(constants.tapsup_token)

print(bot.get_me())
troublemessage = ''


def log(message, answer):
    from datetime import datetime
    print(datetime.now(), end='; ')
    print('Message from {0} {1}; ID: {2}; Text: {3}; '.format(message.from_user.first_name,
                                                            message.from_user.last_name,
                                                            str(message.from_user.id),
                                                            message.text), end='')
    print('Answer:', answer)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    answer = 'Станадртный флоу'
    log(message, answer)

    global troublemessage
    troublemessage= str(datetime.datetime.now()) + '\n'

    keyboard = types.ReplyKeyboardMarkup(True, True, True)
    keyboard.row('/Водитель', '/Комплекс', '/Оператор')
    bot.send_message(message.chat.id, 'У кого проблема?', reply_markup=keyboard)


@bot.message_handler(commands=["Водитель"])
def standart_driver(message):
    global troublemessage
    troublemessage += 'Проблема на стороне водителя\n'
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Подключение', '/Приложение', '/Оплата')
    bot.send_message(message.chat.id, 'С чем у водителей проблема?', reply_markup=keyboard)


@bot.message_handler(commands=["Подключение"])
def driver_connection(message):
    global troublemessage
    troublemessage += 'Проблемы с подключением к системе'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, troublemessage, reply_markup=hide_keyb)


@bot.message_handler(commands=["Приложение"])
def driver_application(message):
    global troublemessage
    troublemessage += 'Проблемы в приложении водителя \n'
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Кнопка', '/Маршрут', '/Другое')
    bot.send_message(message.chat.id, 'Что не работает в приложении?', reply_markup=keyboard)


@bot.message_handler(commands=["Кнопка"])
def application_button(message):
    global troublemessage
    troublemessage += 'В приложении не работает кнопка \n'
    bot.send_message(message.chat.id, troublemessage + 'Допишите комментарий или отправьте заявку')


@bot.message_handler(commands=["Маршрут"])
def application_route(message):
    pass


@bot.message_handler(commands=["Другое"])
def application_other(message):
    pass


@bot.message_handler(commands=["Оплата"])
def driver_payment(message):
    pass


@bot.message_handler(commands=["Комплекс"])
def standart_soft(message):
    pass


@bot.message_handler(commands=["Оператор"])
def standart_oper(message):
    pass


@bot.message_handler(commands=['spec'])
def cmd_spec(message):
    answer = 'Что случилось?'
    log(message, answer)
    bot.send_message(message.chat.id, 'Что случилось?')


@bot.message_handler(commands=['alarm'])
def cmd_alarm(message):
    answer = 'Описание аварии!!!'
    log(message, answer)
    bot.send_message(message.chat.id, 'Описание аварии!!!')


@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    answer = "Hello, #username"
    log(message, answer)

    keyboard = types.ReplyKeyboardMarkup(True, True, True)
    keyboard.row('/start', '/alarm', '/spec')

#    button_start = types.KeyboardButton(text='/start', request_location=True)
#    button_alarm = types.KeyboardButton(text='/alarm')
#    button_spec = types.KeyboardButton(text='/spec')
#    keyboard.add(button_start, button_alarm, button_spec)

#    url_button = types.InlineKeyboardButton(text="go to yandex", url="ya.ru")
#    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Hello, #username", reply_markup=keyboard)
    print(message.text)



if __name__ == '__main__':
    try:
        bot.polling(none_stop = True)
    except Exception:
        time.sleep(15)

'''
def initializeTeleBot():
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)
    telebot.apihelper.proxy = {
      #'http': 'socks5://login:pass@par3.google.385444444444444493392625027464760522671600012331238.proxy.veesecurity.com:443',
      'https': 'socks5://login:pass@par5.google.v98nxnmrtpf8t0oe1j4dcy4tlg636jiv.proxy.veesecurity.com:443'
    }
    bot = telebot.TeleBot(bottoken.token)
    boturl=const.boturl
    #print(bot.get_webhook_info())
    bot.delete_webhook()
    bot.set_webhook(url=boturl)
    print(bot.get_webhook_info())
    return bot
'''
