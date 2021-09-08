AIRTABLE_BASE_ID = ''
AIRTABLE_NAME_ID = ''
AIRTABLE_API_KEY = ''
endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_NAME_ID}'
#python requests headers
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

data = {
  "records": [
    {
      "fields": {
        "Name": "Jastin",
        "Email": "jastin@ya.ru"
      }
    }
  ]
}
#http methods?
#whet is the method for "create" -> HTTP Method POST
import requests
#print(endpoint)
#print(endpoint)

r = requests.post(endpoint, json = data, headers = headers)
print(r.status_code)