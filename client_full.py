import socket
import telebot

token = "TOKEN"

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(
            message.chat.id, "Temp show")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        x = message.text#.lower()
        try:
            if x == 'KEY1':
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(('IP', 1337))
                client.send(x.encode())
                data = client.recv(1024)
                bot.send_message(message.chat.id, data)
                client.close()
            if x == 'KEY2':
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(('IP', 1337))
                client.send(x.encode())
                data = client.recv(1024)
                bot.send_message(message.chat.id, data)
                client.close()
           
        except Exception as ex:
            print(ex)
            bot.send_message(
                message.chat.id,
                "Damn...Something was wrong...")

    bot.polling()
telegram_bot(token)
