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

def bill_game():
    bill = 100;
    my_list = []
    while True:
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