from edadeal import ED
from os import getenv

# библиотека для загрузки данных из env
from dotenv import load_dotenv
import telebot

lenta = ED(CITY = "moskva", SHOP = "lenta-super")#создаем экземпляр класса
pyterochka = ED(CITY = "moskva", SHOP = "5ka")#создаем экземпляр класса
perekrestok = ED(CITY = "moskva", SHOP = "perekrestok")#создаем экземпляр класса
eurospar = ED(CITY = "moskva", SHOP = "eurospar")#создаем экземпляр класса
dixy = ED(CITY = "moskva", SHOP = "dixy")#создаем экземпляр класса

ans = ''

# метода ищет файл env и переменные из него
load_dotenv()
# достает из файла переменную token
token = getenv('token')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    new_text = ["/read - вывести список искомых товаров",
                "/add {Имя товара} - добавить новый товар в список товаров",
                "/del {1,2 .. 10} - удалить товар из списка по номеру",
                "/lenta - поиск товаров из списка со скидками в Лента супермаркет",
                "/5ka - поиск товаров из списка со скидками в Пятерочка",
                "/perek - поиск товаров из списка со скидками в Перекресток",
                "/spar - поиск товаров из списка со скидками в Eurospar",
		        "/dixy - поиск товаров из списка со скидками в Дикси",
                "/all - поиск по всем сформированным файлам и сортировка по цене",
                ]
    bot.reply_to(message, "\n".join(new_text))
@bot.message_handler(commands=['add'])
def add_good(message):
    text_out = 'Пример команды - /add Молоко'
    if len (message.text.split()) > 1:
        text = message.text[4:].lstrip(' ')
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
    text_out = 'Пример команды - /del 0'
    if len (message.text.split()) > 1:
        text = message.text.split()[1]
        lenta.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
        text_out = lenta.del_good_xlsx(text) # удаляем товар из списока по номеру
    chat_id = message.chat.id
    bot.send_message(chat_id, f'{text_out}')
@bot.message_handler(commands=['lenta'])
def search_good5ka(message):
    chat_id = message.chat.id
    lenta.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    bot.send_message(chat_id, f'Ждите, идет запрос ...')
    lenta.get_df_discount()  # запрашиваем список товаров со скидками
    lenta.search()#создаем файл
    lenta.send_file(token,chat_id)#отправляем файл
@bot.message_handler(commands=['5ka'])
def search_good5ka(message):
    chat_id = message.chat.id
    pyterochka.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    bot.send_message(chat_id, f'Ждите, идет запрос ...')
    pyterochka.get_df_discount()  # запрашиваем список товаров со скидками
    pyterochka.search()#создаем файл
    pyterochka.send_file(token,chat_id)#отправляем файл
@bot.message_handler(commands=['perek'])
def search_good5ka(message):
    chat_id = message.chat.id
    perekrestok.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    bot.send_message(chat_id, f'Ждите, идет запрос ...')
    perekrestok.get_df_discount()  # запрашиваем список товаров со скидками
    perekrestok.search()#создаем файл
    perekrestok.send_file(token,chat_id)#отправляем файл
@bot.message_handler(commands=['spar'])
def search_goodspar(message):
    chat_id = message.chat.id
    eurospar.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    bot.send_message(chat_id, f'Ждите, идет запрос ...')
    eurospar.get_df_discount()  # запрашиваем список товаров со скидками
    eurospar.search()#создаем файл
    eurospar.send_file(token,chat_id)#отправляем файл
@bot.message_handler(commands=['dixy'])
def search_gooddixy(message):
    chat_id = message.chat.id
    dixy.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    bot.send_message(chat_id, f'Ждите, идет запрос ...')
    dixy.get_df_discount()  # запрашиваем список товаров со скидками
    dixy.search()#создаем файл
    dixy.send_file(token,chat_id)#отправляем файл
@bot.message_handler(commands=['all'])
def search_all(message):
    chat_id = message.chat.id
    dixy.load_xlsx('goods.xlsx')  # загружаем интересующие нас товары
    bot.send_message(chat_id, f'Ждите, идет объединение файлов ...')
    if not dixy.send_all(token,chat_id):#отправляем файл
        bot.send_message(chat_id, f'Не найдено файлов для объединения!')

@bot.message_handler(func=lambda m: True)
def echo(message):
    print(message)
    bot.reply_to(message, message.text.upper())

bot.infinity_polling()


