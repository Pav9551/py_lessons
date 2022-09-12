from flask import Flask, render_template, request
import requests
import time

from hh_json import parce

# объявление главной переменной
app = Flask(__name__,static_url_path='',
static_folder='dist',
template_folder='dist')


# вывод (редеринг) главной страницы
@app.route('/')
def index():
    dat = {'keywords': '0', 'count': 100, 'down': 260196.25, 'up': 2083139.0,
           'requirements': [{'name': 'грамотная речь', 'count': 52, 'percent': 52.0},
                            {'name': 'работа в команде', 'count': 50, 'percent': 50.0},
                            {'name': 'деловое общение', 'count': 36, 'percent': 36.0},
                            {'name': 'активные продажи', 'count': 25, 'percent': 25.0},
                            {'name': 'навыки продаж', 'count': 25, 'percent': 25.0}], 'vacancy': '0', 'where': 'name',
           'pages': '3'}
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

    dat = {'keywords': '0', 'count': 100, 'down': 260196.25, 'up': 2083139.0, 'requirements': [{'name': 'грамотная речь', 'count': 52, 'percent': 52.0}, {'name': 'работа в команде', 'count': 50, 'percent': 50.0}, {'name': 'деловое общение', 'count': 36, 'percent': 36.0}, {'name': 'активные продажи', 'count': 25, 'percent': 25.0}, {'name': 'навыки продаж', 'count': 25, 'percent': 25.0}], 'vacancy': '0', 'where': 'name', 'pages': '3'}
    print(dat)
    return render_template('results.html', res=dat)
if __name__ == "__main__":
    app.run(debug=True)
