"""
Получение данных от REST сервера
"""
import requests
import pprint

DOMAIN = 'http://127.0.0.1:8000/'
# Отправим запрос на главную страницу
result = requests.get(DOMAIN)

# print(result)

# print('Код ответа от сервера')
# Успешно - 200
# print(result.status_code)

# print('Текст ответа')
# print(result.text)

print('Данные в формате json')
main_url = f'{DOMAIN}cats/cats/'

result = requests.get(main_url)

data = result.json()

pprint.pprint(data)

# print(result.text)


# POST запрос создаст новые данные
result = requests.post(main_url, data={'name': 'Musia', 'breed': 'siam', 'age': 20})

print(result.status_code)

# PUT запрос на изменение данных
result = requests.get(main_url)
# список кошек
cats_list = result.json()
# берем 1-ую
first_cat = cats_list[0]
print(first_cat['name'])
url = first_cat['url']
# отправляем put запрос
result = requests.put(url, data={'name': f'New{first_cat["name"]}', 'age': 2, 'breed': 'NewBreed'})
print(result.status_code)

# options
result = requests.options(url)
print(result.json())

# DELETE запрос
result = requests.delete(url)
print(result.status_code)

#
result = requests.get(main_url)
print(result.text)

# headers
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# }

headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}

result = requests.get(main_url, headers=headers)

print(result.text)
