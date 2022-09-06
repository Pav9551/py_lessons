from flask import Flask, render_template, request
import requests
import time
from hh import HH

# объявление главной переменной
app = Flask(__name__,static_url_path='',
static_folder='dist',
template_folder='dist')


# вывод (редеринг) главной страницы
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

# вывод страницы формы
@app.route('/results/')
def form():
    return render_template('results.html')
