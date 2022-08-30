from edadeal import ED
import requests
from os import getenv
from os.path import exists

# библиотека для загрузки данных из env
from dotenv import load_dotenv
import telebot

# файл дляпарсинга данных
from digital import parce


lenta = ED(CITY = "moskva", SHOP = "lenta-super")#создаем экземпляр класса
pyterochka = ED(CITY = "moskva", SHOP = "5ka")#создаем экземпляр класса
perekrestok = ED(CITY = "moskva", SHOP = "perekrestok")#создаем экземпляр класса
eurospar = ED(CITY = "moskva", SHOP = "eurospar")#создаем экземпляр класса
ans = ''

# метода ищет файл env и переменные из него
load_dotenv()
# достает из файла переменную token
token = getenv('token')
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = message.text.split()[1]
    bot.reply_to(message, text[::-1])
@bot.message_handler(commands=['add'])
def add_good(message):
    text = 'Пример команды - /add Молоко'
    if len (message.text.split()) > 1:
        text = message.text.split()[1]
        lenta.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
        text_out = lenta.add_xlsx(text) # добавляем товар в общий список
    chat_id = message.chat.id
    bot.send_message(chat_id, f'{text_out}')

@bot.message_handler(commands=['read'])
def read_goods(message):
    lenta.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    chat_id = message.chat.id
    bot.send_message(chat_id, f'{lenta.excel_data_df.name}')
@bot.message_handler(commands=['del'])
def delete_good(message):
    text = 'Пример команды - /del {0,1,2..10}'
    if len (message.text.split()) > 1:
        text = message.text.split()[1]
        lenta.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
        text_out = lenta.del_good_xlsx(text) # удаляем товар из списока по номеру
    chat_id = message.chat.id
    bot.send_message(chat_id, f'{text_out}')
@bot.message_handler(commands=['lenta'])
def search_good(message):

    chat_id = message.chat.id
    lenta.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    bot.send_message(chat_id, f'Ждите, идет запрос ...')
    lenta.get_df_discount()  # запрашиваем список товаров со скидками
    filename = lenta.search()
    url = f'https://api.telegram.org/bot{token}/'
    method = url + 'sendDocument'
    if exists(filename):
        with open(filename, "rb") as filexlsx:
            files = {"document": filexlsx}
            title = filename
            r = requests.post(method, data={"chat_id": chat_id, "caption": title}, files=files)
            if r.status_code != 200:
                raise Exception("send error")
    else:
        bot.send_message(chat_id, 'Файл не сформирован.')


'''@bot.message_handler(commands=['parse'])
def parse_site(message):
    text = message.text.split()[1]
    chat_id = message.chat.id
    q = parce(text)
    for it in q[:20]:
        bot.send_message(chat_id, f'{it[0]} - {it[1]}')


@bot.message_handler(commands=['file'])
def send_file(message):
    chat_id = message.chat.id
    if exists('base.csv'):
        with open('base.csv') as f:
            bot.send_document(chat_id, f)
    else:
        bot.send_message(chat_id, 'Файл не сформирован. Используйте команду /parce для его формирования')

'''
@bot.message_handler(func=lambda m: True)
def echo(message):
    print(message)
    bot.reply_to(message, message.text.upper())


bot.infinity_polling()


