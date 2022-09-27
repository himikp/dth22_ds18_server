import socket
import telebot

token = "5630470185:AAFUxWgoT_3AiKYtdtPAUvZne95xWuyTI6s"

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(('192.168.8.117', 1337))

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(
            message.chat.id, "Бот показує температуру")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        x = message.text#.lower()
        try:
            if x == 'room':
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(('192.168.8.117', 1337))
                client.send(x.encode())
                data = client.recv(1024)
                bot.send_message(message.chat.id, data)
                client.close()
            if x == 'street':
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(('192.168.8.140', 1337))
                client.send(x.encode())
                data = client.recv(1024)
                bot.send_message(message.chat.id, data)
                client.close()
            #else:
                #bot.send_message(message.chat.id, 'Ups! I dont know what you want! Enter room or street for get temp')
        except Exception as ex:
            print(ex)
            bot.send_message(
                message.chat.id,
                "Damn...Something was wrong...")

    bot.polling()
telegram_bot(token)
# while True:
#     message = input('Enter your message: ')
#         
#     if message == '!q':
#         client.close()
#         break
#     else:
#         client.send(message.encode())
#         data = client.recv(1024)
#         print (data)
