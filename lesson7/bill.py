"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import json

def create_json(bill, my_list):
    name = 'bill_json.txt'
    save_data = {
        'bill': bill,
        'list': my_list,
    }
    load_data = {
        'bill': 0,
        'list': [],
    }
    src_answer = os.path.join(os.getcwd(), name)
    if not os.path.exists(src_answer):
        print("Это первый запуск. Создаем файл")
        with open( name, 'w', encoding='utf-8') as f:
            f.write(json.dumps(save_data))
            f.close()
        with open(name, 'r', encoding='utf-8') as f:
            load_data = json.load(f)
            f.close()
    else:
        with open(name, 'r', encoding='utf-8') as f:
            load_data = json.load(f)
            f.close()
    return load_data

def save_json(bill, my_list):
    name = 'bill_json.txt'
    save_data = {
        'bill': bill,
        'list': my_list,
    }
    with open(name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(save_data))
        f.close()

def bill_game():
    bill = 0;
    my_list = []
    load_data = create_json(bill, my_list)
    bill = load_data['bill']
    my_list = load_data['list']
    while True:
        save_json(bill, my_list)
        print('На Вашем счете: {} руб.'.format(bill))
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню:')
        if choice == '1':
            print('Введите сумму пополнения: ')
            add = int(input())  # ввод
            bill = add + bill;
            pass
        elif choice == '2':
            print('Введите сумму покупки: ')
            cost = int(input())  # ввод
            if cost > bill:
                print('денег не хватает.')
            else:
                print('Введите название покупки: ')
                bay = input()  # ввод
                bill = bill - cost
                st = str(bay) + ':' + str(cost) + 'р.'
                my_list.append(st)
            pass
        elif choice == '3':
            print('Список покупок: ')
            for number in my_list:
                print('----- {}'.format(number))
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')