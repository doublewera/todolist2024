from todolist.secret import token
import telebot

class MyBot(telebot.TeleBot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__users = {}
        try:
            self.__load_users()
        except:
            print('No users')
    
    def add_user(self, msg):
        if msg.chat.id not in self.__users:
            self.__users[msg.chat.id] = ''
            self.__save_users()

    def __save_users(self):
        f = open('my_users.txt', 'w')
        for u in self.__users:
            f.write(str(u) + '\n')
        f.close()
    
    def __load_users(self):
        f = open('my_users.txt')
        for line in f:
            self.__users[line] = ''
        f.close()


bot = MyBot(token)

@bot.message_handler(commands= ['start'])
def start(message):
    print ("В консоль: начало работы")
    bot.add_user(message)
    bot.send_message(
        message.chat.id,
        '<b>Пользователю: готов!</b>', parse_mode='html')
    
bot.polling(none_stop=True)