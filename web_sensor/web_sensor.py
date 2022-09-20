import os, time
from bottle import route, run, template


def cpu_temp():
    try:
        dev = os.popen('sensors')
        cpu_temp = dev.read().split(' ')[6][1:-2]
    except:
        cpu_temp ='50.0'
        print('sudo apt-get install lm-sensors')
    return cpu_temp

@route('/temp')
def temp():
    return cpu_temp()
	
@route('/')
def index():
	return template('main.html')
	
@route('/raphael')
def index():
	return template('raphael.2.1.0.min.js')

@route('/justgage')
def index():
	return template('justgage.1.0.1.min.js')

run(host='127.0.0.1', port=8070)