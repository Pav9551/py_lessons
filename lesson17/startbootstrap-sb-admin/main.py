from flask import Flask, render_template, request
from flask_apscheduler import APScheduler
from pymongo import MongoClient
import requests
import time

from hh_json import parce
count = 1
dat = {'keywords': '0', 'count': 100, 'down': 260196.25, 'up': 2083139.0,
       'requirements': [{'name': 'грамотная речь', 'count': 52, 'percent': 52.0},
                        {'name': 'работа в команде', 'count': 50, 'percent': 50.0},
                        {'name': 'деловое общение', 'count': 36, 'percent': 36.0},
                        {'name': 'активные продажи', 'count': 25, 'percent': 25.0},
                        {'name': 'навыки продаж', 'count': 25, 'percent': 25.0}], 'vacancy': '0', 'where': 'name',
       'pages': '3'}
# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True
# объявление главной переменной
app = Flask(__name__,static_url_path='',
static_folder='dist',
template_folder='dist')

app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True


scheduler.init_app(app)
scheduler.start()
# interval example
@scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
def job1():
    USERNAME = 'n8n'
    PASSWORD = 'Lb5e'
    CLUSTER = 'cluster0.hmewc.mongodb.net'

    DATABASE = 'local'

    CONNECTION_STRING = f"mongodb+srv://ivan:5ri6y7syzbEB086c@cluster0.2svumdh.mongodb.net/test?authSource=admin&replicaSet=atlas-11ptof-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
    client = MongoClient(CONNECTION_STRING)
    db = client['db']
    collection = db['hotel1room1db']
    Name = "\u0423\u0420\u0410\u041D123"
    temperature = 285
    humidity = 17
    MQ2 = 228
    Sound = 156
    motion_count = 0
    sound_count = 0
    street = 'Lenina'
    number = 1
    city = 'Moscow'
    data = {'Data': '13_сентября',
            'count': 2,
            'total': 12,
            'per': int(2/12*100)
            }
    insert_result = collection.insert_one(data)
    insert_result
    print(client.list_database_names())

    client.close()
    print('Job 1 executed')


# вывод (редеринг) главной страницы
@app.route('/')
@app.route('/index')
def index():

    print(dat)
    return render_template('index.html', res=dat)


# вывод страницы формы
@app.route('/form/')
def form():
    return render_template('form.html')


@app.post('/result/')
def result():
    """
    Вывод результата обработки запроса
    :return: страница с результатами
    """
    #vac = request.form
    #data = parce(**vac)
    #dat = {**data, **vac}  # data | vac - в Python 3.10 можно сделать так

    #dat = {'keywords': '0', 'count': 100, 'down': 260196.25, 'up': 2083139.0, 'requirements': [{'name': 'грамотная речь', 'count': 52, 'percent': 52.0}, {'name': 'работа в команде', 'count': 50, 'percent': 50.0}, {'name': 'деловое общение', 'count': 36, 'percent': 36.0}, {'name': 'активные продажи', 'count': 25, 'percent': 25.0}, {'name': 'навыки продаж', 'count': 25, 'percent': 25.0}], 'vacancy': '0', 'where': 'name', 'pages': '3'}
    print(dat)
    return render_template('results.html', res=dat)
if __name__ == "__main__":
    app.run(debug=True)
