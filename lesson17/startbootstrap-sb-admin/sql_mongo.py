import requests
import psycopg2
import json
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
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
  dict_room = {room: {'loud':fetch[0][0],'count':fetch[1][0]}}
  return dict_room
def to_mongo():
  dict_rooms = {}
  for item in ['room1','room2','room3','room4','room5','room6','room7','room8','room9','room10','corridor1','corridor2','cab1']:
    dict_rooms.update(from_base(room = item))
  client = MongoClient(CONNECTION_STRING)
  db = client['db']
  collection = db['sound']
  data = dict_rooms.copy()
  insert_result = collection.insert_one(data)
  print(dict_rooms)
  client.close()
  return insert_result


