from flask import Flask, render_template, request
import requests
import time
from hh_json import parce
from crud import read_skills
from crud import add_row
from crud import clear_base


# объявление главной переменной
app = Flask(__name__,static_url_path='',
static_folder='dist',
template_folder='dist')

# вывод (редеринг) главной страницы
@app.route('/')
def index():
    out_text = {'name': read_skills()}
    return render_template('index.html', sql_qwery = out_text)
@app.post('/clear/')
def clear():
    clear_base()
    return render_template('clear.html')
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
    dat['where'] = 'в названии вакансии' \
        if dat['where'] == 'name' else 'в названии компании' if dat['where'] == 'company' else 'везде'
    add_row(dat)
    return render_template('results.html', res=dat)
#if __name__ == "__main__":
    #app.run(debug=True)
