from loto_lib import *
def help_command():
    print('---------------------------------------------')
    print('          Игра ЛОТО:')
    print(' 1 - Играть против компьютера')
    print(' 2 - Играть против друг-друга')
    print(' 3 - Компьютер против компьютера')
    print(' help - для вывода списка меню')
    print(' 0 / stop - Выход')
    print('---------------------------------------------')
def comp_vs_comp():
    print('Режим компьютер против компьютера:')
    #создаем мешок с боченками
    our_bag = Bag()
    #создаем карту для компьютера 1
    Card1 = Card("Компьютер 1")
    # создаем карту для компьютера 2
    Card2 = Card("Компьютер 2")
    Card1.show_card()
    Card2.show_card()
    print('Начинаем игру:')
    while ((Card1.win == False) and (Card2.win == False)):
        barrel = our_bag.get_barrel()#тянем боченок
        print(f'Новый боченок номер {barrel},в мешке осталось: {len(our_bag)}')
        Card1.strike_out_computer(barrel)#зачеркиваем
        Card2.strike_out_computer(barrel)#зачеркиваем
        Card1.show_card()#показываем
        Card1.check_win_card()#проверяем победителя
        Card2.show_card()#показываем
        Card2.check_win_card()#проверяем победителя
    if ((Card1.win == True) and (Card2.win == True)):
        print('Ничья')
    else:
        if (Card1.win == True):
            print('Выйграл компьютер 1')
        if (Card2.win == True):
            print('Выйграл компьютер 2')
def user_vs_comp():
    print('Режим игрок против компьютера:')
    #создаем мешок с боченками
    our_bag = Bag()
    #создаем карту для компьютера 1
    Card1 = Card("Игрок 1")
    # создаем карту для компьютера 2
    Card2 = Card("Компьютер 2")
    Card1.show_card()
    Card2.show_card()
    print('Начинаем игру:')
    while ((Card1.win == False) and (Card2.win == False)):
        barrel = our_bag.get_barrel()#тянем боченок
        print(f'Новый боченок номер {barrel},в мешке осталось: {len(our_bag)}')
        answer = (input(f'Игрок 1, зачеркнуть цифру {barrel} ? (y/n): ') == 'y')
        Card1.strike_out_user(barrel,answer)#зачеркиваем
        Card2.strike_out_computer(barrel)#зачеркиваем
        Card1.show_card()#показываем
        Card1.check_win_card()#проверяем победителя
        Card2.show_card()#показываем
        Card2.check_win_card()#проверяем победителя
        if (Card1.in_game == False):
            Card1.win = False
            Card2.win = True
            print('Игрок 1 проиграл.')
    if ((Card1.win == True) and (Card2.win == True)):
        print('Ничья')
    else:
        if (Card1.win == True):
            print('Выйграл игрок 1')
        if (Card2.win == True):
            print('Выйграл компьютер 2')
def user_vs_user():
    print('Режим друг против друга:')
    #создаем мешок с боченками
    our_bag = Bag()
    #создаем карту для компьютера 1
    Card1 = Card("Игрок 1")
    # создаем карту для компьютера 2
    Card2 = Card("Игрок 2")
    Card1.show_card()
    Card2.show_card()
    print('Начинаем игру:')
    while ((Card1.win == False) and (Card2.win == False)):
        barrel = our_bag.get_barrel()#тянем боченок
        print(f'Новый боченок номер {barrel},в мешке осталось: {len(our_bag)}')
        answer1 = (input(f'Игрок 1, зачеркнуть цифру {barrel} ? (y/n): ') == 'y')
        Card1.strike_out_user(barrel,answer1)#зачеркиваем
        if (Card1.in_game == False):
            Card1.win = False
            Card2.win = True
            print('Игрок 1 проиграл.')
            break
        answer2 = (input(f'Игрок 2, зачеркнуть цифру {barrel} ? (y/n): ') == 'y')
        Card2.strike_out_user(barrel,answer2)#зачеркиваем
        if (Card2.in_game == False):
            Card1.win = True
            Card2.win = False
            print('Игрок 2 проиграл.')
            break
        Card1.show_card()#показываем
        Card1.check_win_card()#проверяем победителя
        Card2.show_card()#показываем
        Card2.check_win_card()#проверяем победителя
    if ((Card1.win == True) and (Card2.win == True)):
        print('Ничья')
    else:
        if (Card1.win == True):
            print('Выйграл игрок 1')
        if (Card2.win == True):
            print('Выйграл игрок 2')
response = 'N'# Переменная на выход
# Меню программы
while response != 'stop':
    help_command();
    response = input('Укажите номер пункта меню (help - для вывода списка меню) -> ')
    if response == '1':  # Играть против компьютера
        user_vs_comp()
        pass
    elif response == '2':  # Играть против друг-друга
        user_vs_user()
        pass
    elif response == '3':  # Компьютер против компьютера
        comp_vs_comp()
        pass

    elif (response.lower() == 'help'):  # help
        help_command();
        pass
    elif (response == '0') or (response.lower() == 'stop'):  # Выход
        print('Выход из программы...')
        break
    else:
        print("Повторите ввод.")