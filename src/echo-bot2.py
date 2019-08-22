# -*- coding: utf-8 -*-
import constants
import telebot
import datetime
import time
from telebot import types


bot = telebot.TeleBot(constants.tapsup_token)

class tr_message:
    def __init__(self, msgstart = False):
        self.is_start = msgstart
    t_message = 'Обращение в службу поддержки \n'

print(bot.get_me())
troublemessage = ''

tb_msg = tr_message(msgstart=False)

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

    tb_msg.is_start = True
    tb_msg.t_message += str(datetime.datetime.now()) + '\n'
    tb_msg.t_message += 'Message from {0} {1}; AKA {2} ID: {3}; From chat: {4}; \n'.format(message.from_user.first_name,
                                                            message.from_user.last_name,
                                                            message.from_user.username,
                                                            str(message.from_user.id),
                                                            message.chat.title)
    print(str(message))

    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к списку заявок", url="http://help.373soft.ru/issues")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

    keyboard = types.ReplyKeyboardMarkup(True, True, True)
    keyboard.row('/Водитель')
    keyboard.row('/Комплекс')
    keyboard.row('/Оператор')
    ans = bot.send_message(message.chat.id, 'У кого проблема?', reply_markup=keyboard)

    #bot.register_next_step_handler(ans, standart_driver)

@bot.message_handler(commands=["chatid"])
def cmd_chatid(message):
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, message.chat.id, reply_markup=hide_keyb)


@bot.message_handler(commands=["Водитель"])
def standart_driver(message):
    tb_msg.t_message += 'Проблема на стороне водителя\n'

    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Подключение')
    keyboard.row('/Приложение')
    keyboard.row('/Оплата')
    bot.send_message(message.chat.id, 'С чем у водителей проблема?', reply_markup=keyboard)


@bot.message_handler(commands=["Подключение"])
def driver_connection(message):
    tb_msg.t_message += 'Проблемы с подключением к системе\n'
    msg = 'Дополните информацию: позывные, все водители или единичный случай, еще какие-то особенности и подробности'

    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=["Приложение"])
def driver_application(message):
    tb_msg.t_message += 'Проблемы в приложении водителя \n'

    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Кнопка')
    keyboard.row('/Маршрут')
    keyboard.row('/Другое')
    bot.send_message(message.chat.id, 'Что не работает в приложении?', reply_markup=keyboard)


@bot.message_handler(commands=["Кнопка"])
def application_button(message):
    tb_msg.t_message += 'В приложении не работает кнопка \n'
    msg = 'Дополните информацию: позывные, все водители или единичный случай, еще какие-то особенности и подробности'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)

@bot.message_handler(commands=["Маршрут"])
def application_route(message):
    tb_msg.t_message += 'В приложении не корректно расчитывается маршрут \n'
    msg = 'Дополните информацию: позывные, все водители или единичный случай, еще какие-то особенности и подробности'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=["Другое"])
def application_other(message):
    tb_msg.t_message += 'Приложение работает не корректно \n'
    msg = 'Дополните информацию: позывные, все водители или единичный случай, еще какие-то особенности и подробности'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=["Оплата"])
def driver_payment(message):
    tb_msg.t_message += 'Проблемы с оплатой у водителя \n'
    msg = 'Дополните информацию: позывные, все водители или единичный случай, еще какие-то особенности и подробности'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=["Комплекс"])
def standart_soft(message):
    tb_msg.t_message += 'Проблема с комплекосм\n'
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Телефония')
    keyboard.row('/Приложение')
    bot.send_message(message.chat.id, 'Какя часть комплекса не работает?', reply_markup=keyboard)


@bot.message_handler(commands=["Телефония"])
def soft_phone(message):
    tb_msg.t_message += 'Проблема с телефонией\n'
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Входящая')
    keyboard.row('/Исходящая')
    keyboard.row('/Блокировка')
    bot.send_message(message.chat.id, 'Какое направление телефонии требует внимания?', reply_markup=keyboard)


@bot.message_handler(commands=["Входящая"])
def phone_in(message):
    tb_msg.t_message += 'Проблема с входящими звонками\n'
    msg = 'Допишите комментарий с какого момента не работает и отправьте заявку кнопкой /Готово'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=["Исходящая"])
def phone_out(message):
    tb_msg.t_message += 'Проблема с отзвонами\n'
    msg = 'Допишите комментарий с какого момента не работает, по всем каналам или нет и отправьте заявку кнопкой /Готово'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=["Блокировка"])
def phone_block(message):
    tb_msg.t_message += 'Заблокировать абонента\n'
    msg = 'Допишите кого и по какой причине заблокировать и отправьте заявку кнопкой /Готово'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=["Оператор"])
def oper(message):
    tb_msg.t_message += 'Проблема с местом оператора\n'

    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('/Не работает ПК')
    keyboard.row('/Проблема с таксиофисом')
    keyboard.row('/Не работает гарнитура')
    keyboard.row('/Не верное время')
    bot.send_message(message.chat.id, 'Что не работает?', reply_markup=keyboard)


@bot.message_handler(commands=['/Не работает ПК'])
def oper_pc(message):
    print('operator PC')
    tb_msg.t_message += 'Не работает ПК \n'
    msg = 'Сообщите номер ПК и отправьте заявку кнопкой /Готово'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=['/Проблема с таксиофисом'])
def oper_taxioffice(message):
    print('taxioffice troubles')
    tb_msg.t_message += 'Проблема с таксиофисом \n'
    msg = 'Сообщите номер ПК где не работает комплекс и отправьте заявку кнопкой /Готово'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=['/Не работает гарнитура'])
def oper_garniture(message):
    print('garniture troubles')
    tb_msg.t_message += 'Не работает гарнитура \n'
    msg = 'Сообщите номер ПК где не работает гарнитура и отправьте заявку кнопкой /Готово'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


@bot.message_handler(commands=['/Не верное время'])
def oper_pctime(message):
    print('pc time troubles')
    tb_msg.t_message += 'Не верное время на ПК \n'
    msg = 'Сообщите номер ПК с некорректным временем и отправьте заявку кнопкой /Готово'
    hide_keyb = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, msg, reply_markup=hide_keyb)


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


@bot.message_handler(commands=['Готово'])
def done_ask(message):
    #global troublemessage
    #troublemessage += str(message.text)
    tb_msg.is_start = False

    keyboard = types.ReplyKeyboardMarkup(True, True, True)
    keyboard.row('/start', '/alarm', '/spec')
    bot.send_message(message.chat.id, tb_msg.t_message, reply_markup=keyboard)
    tb_msg.t_message = ''


@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
#    answer = "Hello, #username"
#    log(message, answer)

    if tb_msg.is_start:
        tb_msg.t_message += message.text

        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('/Готово')
        msg = 'Дополните описание проблемы, если больше нечего добавить, нажмите /Готово'
    else:
        keyboard = types.ReplyKeyboardMarkup(True, True, True)
        keyboard.row('/start', '/alarm', '/spec')

#    button_start = types.KeyboardButton(text='/start', request_location=True)
#    button_alarm = types.KeyboardButton(text='/alarm')
#    button_spec = types.KeyboardButton(text='/spec')
#    keyboard.add(button_start, button_alarm, button_spec)

#    url_button = types.InlineKeyboardButton(text="go to yandex", url="ya.ru")
#    keyboard.add(url_button)
        msg = "Hello, " + str(message.from_user.username)
    bot.send_message(message.chat.id, msg, reply_markup=keyboard)
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
