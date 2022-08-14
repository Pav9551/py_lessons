AIRTABLE_BASE_ID = 'appbtZQhnZqNKg4FB'
AIRTABLE_NAME_ID = 'Table%201'
AIRTABLE_API_KEY = 'keyubxjXqAckKCoY0'

endpoint = f'https://maker.ifttt.com/trigger/1/with/key/fXHXLeRKLkPLoOgv_z0cl7QoasGw1WDW9lbrmq9QTaa'
#python requests headers
headers = {'Content-Type': 'application/json'}
v1 = 1
data = {"value1":v1,"value2":v1,"value3":v1}

#http methods?
#whet is the method for "create" -> HTTP Method POST
import requests

r = requests.post(endpoint, json = data, headers = headers)
print(r.status_code)
print(data)