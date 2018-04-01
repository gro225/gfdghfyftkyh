from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

getting = {}

id_array = []

updater = Updater(token = '580322629:AAHCc2Kp3Icq3eiPA4iiNGV7ok9eLpoZmV0')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = ' общаться?')
def helpCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = 'Итак, на сегоднешнний день я умею: 1.Определить можно ли построить треугольник с помощью команды(Triangle) 2.Найти корень числа с помощью команды (Реши) 3.Является ли треугольник прямоугольным с помощью команды(Прям)')
def textMessage(bot, update):
    if (update.message.chat_id not in id_array):
        id_array.append(update.message.chat_id)
        getting[update.message.chat_id] = []
    print(getting) 
    getting[update.message.chat_id].append(update.message.text)
    if (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "Triangle"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите стороны треугольника")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "Triangle"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        c = int(string[2])
        if (a < b+c) and (b < c+a) and (c < b+a):
            bot.send_message(chat_id = update.message.chat_id, text = "Можно")
        else:
            bot.send_message(chat_id = update.message.chat_id, text = "Нельзя")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "Реши"):
        bot.send_message(chat_id = update.message.chat_id, text = "Введите a b c")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "Реши"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        c = int(string[2])
        d = b*b - 4*a*c
        x1 = (-b + d**(1/2))/(2*a)
        x2 = (-b - d**(1/2))/(2*a)
        res = "x1 = "+str(x1)+" x2 = "+str(x2)
        bot.send_message(chat_id = update.message.chat_id, text = res)
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "Прям"):
         bot.send_message(chat_id = update.message.chat_id, text = "Введите стороны треугольника")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "Прям"):
        string = getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1].split()
        a = int(string[0])
        b = int(string[1])
        c = int(string[2])
        if (a**2==(b**2 + c**2)) or (b**2==(a**2 + c**2)) or (c**2==(a**2 + b**2)):
            bot.send_message(chat_id = update.message.chat_id, text = "Пямоугольный")
        else:
            bot.send_message(chat_id = update.message.chat_id, text ='Не прямоугольный')
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 1] == "Код"):
         bot.send_message(chat_id = update.message.chat_id, text = "Какое слово закодировать?")
    elif (getting[update.message.chat_id][len(getting[update.message.chat_id]) - 2] == "Код"):
        string = getting[update.message.chat_id]
        print(1)
        bits= int(string, 2)
        print(1)
        bot.send_message(chat_id = update.message.chat_id, text = bits)
    else:
        res = 'Получил ваше сообщение: '+ update.message.text
        bot.send_message(chat_id = update.message.chat_id, text = res)
start_handler =CommandHandler ('start', startCommand)
text_handler = MessageHandler(Filters.text, textMessage)
help_handler = CommandHandler('help', helpCommand)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)
dispatcher.add_handler(help_handler)

updater.start_polling(clean=True)

updater.idle()
