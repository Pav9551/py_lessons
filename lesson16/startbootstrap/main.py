from flask import Flask, render_template, request
import requests
import time
from hh import HH
from hh_json import parce

# объявление главной переменной
app = Flask(__name__,static_url_path='',
static_folder='dist',
template_folder='dist')


# вывод (редеринг) главной страницы
@app.route('/')
def index():
    return render_template('index.html')


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
    vac = request.form
    data = parce(**vac)
    dat = {**data, **vac}  # data | vac - в Python 3.10 можно сделать так
    print(dat)
    return render_template('results.html', res=dat)
if __name__ == "__main__":
    app.run(debug=True)
