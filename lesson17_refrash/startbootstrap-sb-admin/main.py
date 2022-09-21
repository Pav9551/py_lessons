from flask import Flask, render_template, request, redirect, url_for
from flask_apscheduler import APScheduler
from sql_mongo import to_mongo,from_mongo
#from flask_bootstrap import Bootstrap
count = 1

def cpu_temp():
    try:
        dev = os.popen('sensors')
        cpu_temp = dev.read().split(' ')[6][1:-2]
    except:
        cpu_temp ='50.0'
        print('sudo apt-get install lm-sensors')
    return cpu_temp
# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True
# объявление главной переменной
app = Flask(__name__,static_url_path='',
static_folder='dist',
template_folder='dist')
#bootstrap = Bootstrap(app)
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
    to_mongo()
    #print('Job 1 executed')

@app.route('/temp')
def index1():
    dat, time = from_mongo()
    rooms = dat.copy()
    rooms.pop('_id')
    total = []
    above0pr = []
    above10pr = []
    above20pr = []
    count = 0
    for k , v in rooms.items():
        if k != 'тестовое':
            #print(k,v['count'])
            if v['count'] > 0:
                total.append(k)
                count = count + 1
                loudper = v['loud']/v['count']*100
                if (loudper > 0) and (loudper < 10):
                    above0pr.append(k)
                if (loudper >= 10) and (loudper < 20):
                    above10pr.append(k)
                if (loudper >= 20):
                    above20pr.append(k)

    str = ','.join(total)
    strabove0pr = ','.join(above0pr)
    strabove10pr = ','.join(above10pr)
    strabove20pr = ','.join(above20pr)
    per = int(count/12*100)
    summary = f"Сейчас работает {per} % устройств, а именно: {str}."
    success = f"Незначительный шум в помещениях: {strabove0pr}."
    warning = f"Умеренный шум в помещениях: {strabove10pr}."
    danger = f"Внимание! Превышение более 20%: {strabove20pr}."

    if len(above0pr) == 0:
        success = f"Помещений с незначительным шумом не найдено."
    if len(above10pr) == 0:
        warning = f"Помещений с превышением 10% не найдено."
    if len(above20pr) == 0:
        danger  = f"Помещений с превышением 20% не найдено."

    if len(above0pr) == 1:
        success = f"Незначительный шум в помещении {strabove0pr}."
    if len(above10pr) == 1:
        warning = f"Умеренный шум в помещении {strabove10pr}."
    if len(above20pr) == 1:
        danger  = f"Внимание! Превышение более 20% в {strabove20pr}."

    dictsummary = dict(primary = summary,success = success,warning = warning,danger = danger)
    return dictsummary

# вывод (редеринг) главной страницы
@app.route('/')
@app.route('/index.html')
def index():
    dat, time = from_mongo()
    rooms = dat.copy()
    rooms.pop('_id')
    return render_template('index.html', res=rooms, time = time)
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

    dat = {'keywords': '0', 'count': 100, 'down': 260196.25, 'up': 2083139.0, 'requirements': [{'name': 'грамотная речь', 'count': 52, 'percent': 52.0}, {'name': 'работа в команде', 'count': 50, 'percent': 50.0}, {'name': 'деловое общение', 'count': 36, 'percent': 36.0}, {'name': 'активные продажи', 'count': 25, 'percent': 25.0}, {'name': 'навыки продаж', 'count': 25, 'percent': 25.0}], 'vacancy': '0', 'where': 'name', 'pages': '3'}
    print(dat)
    return render_template('results.html', res=dat)
if __name__ == "__main__":
    app.run(debug=True)
