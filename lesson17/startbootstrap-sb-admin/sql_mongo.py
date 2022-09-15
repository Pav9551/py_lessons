import requests
import psycopg2
import json
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()
host = getenv('host')
port = getenv('port')
dbname = getenv('dbname')
user = getenv('user')
password = getenv('password')
CONNECTION_STRING = getenv('CONNECTION_STRING')
#print(CONNECTION_STRING)
def from_base(host=host, port=port, room = 'room1'):
  conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
  cur = conn.cursor()
  #количество строк в таблице
  #cur.execute("SELECT count(*) FROM public.states")
  loud = f"public.states WHERE entity_id='sensor.{room}_sound'  and state < '3.00' and state > '2.00' and last_changed  >=  now() - interval '1 hours 00 minutes'"
  all = f"public.states WHERE entity_id='sensor.{room}_sound'  and state < '3.00' and state > '0.00' and last_changed  >=  now() - interval '1 hours 00 minutes'"
  cur.execute(f"SELECT count(state) FROM {loud} UNION ALL SELECT count(state) FROM {all}")
  fetch = cur.fetchall()
  conn.close()
  #количество превышений и общее количество измерений уровня звука
  percent = 0
  if fetch[1][0] > 0:
    percent = int(fetch[0][0]/fetch[1][0]*100)#процент шумных значений
  roomnames = {'room1': '№101', 'room2': '№102', 'room3': '№103', 'room4': '№104', 'room5': '№105', 'room6': '№106',
                'room7': '№107', 'room8': '№108', 'room9': '№109',
                'room10': '№110', 'corridor1': 'Коридор 1', 'corridor2': 'Коридор 2', 'cab1': 'тестовое'}
  dict_room = {roomnames[room]: {'loud':fetch[0][0],'count':fetch[1][0],'percent':percent}}
  return dict_room
def to_mongo():
  dict_rooms = {}
  for item in ['room1','room2','room3','room4','room5','room6','room7','room8','room9','room10','corridor1','corridor2','cab1']:
    dict_rooms.update(from_base(room = item))#добавляем в словарь результаты запросов
  client = MongoClient(CONNECTION_STRING)
  db = client['db']
  collection = db['sound']
  data = dict_rooms.copy()
  insert_result = collection.insert_one(data)
  client.close()
  return insert_result

def from_mongo():
  client = MongoClient(CONNECTION_STRING)
  db = client['db']
  collection = db['sound']
  #read_db = db.get_collection('sound').find_one()
  #read_db = db.get_collection('sound').find().sort([('_id', -1)]).limit(1)
  #read_db = db.sound.find().sort([('_id', -1)]).limit(1)
  record = list(db.sound.find().sort([('_id', -1)]).limit(1))
  recordcopy = record.copy()
  HOUR = timedelta(hours=3)
  time = recordcopy[0].get('_id').generation_time + HOUR
  #time = time.strftime("%A, %d. %B %Y %I:%M%p")
  time = time.strftime("%m %d %Y, %H:%M:%S")

  client.close()
  return record[0] , time







