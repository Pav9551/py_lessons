import requests
import pprint

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'

params = {
    'text': 'C# developer',
#     # страница
    'page': 1
}
#
# result = requests.get(url_vacancies, params=params).json()
#
# items = result['items']
#
# first = items[0]
#
# #pprint.pprint(first)
#
# print(first['alternate_url'])
# one_vacancy_url = first['url']
#
# result = requests.get(one_vacancy_url, params=params).json()
#
# pprint.pprint(result)

params = {
   #'text': 'NAME:(Python OR Java) AND COMPANY_NAME:(1 OR 2 OR Yandex) AND (Django OR Spring)',
   'text': 'NAME:(Python)' ,
    #страница
    'page': 1
}

'''result = requests.get(url_vacancies, params=params).json()
items = result['items']
#
first = items[0]
#pprint.pprint(result)

print(first['alternate_url'])
one_vacancy_url = first['url']'''
result = requests.get(url_vacancies, params=params).json()
pprint.pprint(result)


