import numpy as np
def zero_and_ones():
    zero_arr = np.zeros(4)
    ones_arr = np.ones(5)
    zero_and_ones = np.concatenate((zero_arr, ones_arr))
    np.random.shuffle(zero_and_ones)
    return zero_and_ones

class Bag:
    def __init__(self):
        number_of_barrels = 91
        numbers = np.arange(1, number_of_barrels)
        np.random.shuffle(numbers)
        self.numbers = numbers
        self.current_barrel = self.numbers[0]
    def __str__(self):
        return f'Номера бочонков по порядку вытаскивания:{self.numbers}'

    def __len__(self):
        return len(self.numbers)
    def get_barrel(self):
        self.current_barrel = self.numbers[0]
        if len(self.numbers) > 1:
            self.numbers = np.delete(self.numbers, 0)
        return self.current_barrel

class Card:
    def __init__(self, user):
        numbers = np.arange(1, 91)
        np.random.shuffle(numbers)
        rand_arr = numbers[:27]
        rand_01 = np.concatenate((zero_and_ones(), zero_and_ones(), zero_and_ones()))
        self.numbers = rand_arr * rand_01
        self.numbers = np.int8(self.numbers)
        self.win = False
        self.in_game = True
        self.good_answer = True
        self.arr = self.numbers
        self.user = user
    def show_card(self):
        print(f'--------карточка {self.user}--------')
        #print(np.reshape(self.numbers, (3, 9)))
        #print(self.numbers[:9])
        #print(self.numbers[9:18])
        #print(self.numbers[18:29])

        self.arr = np.where(self.numbers == 0, '', np.where(self.numbers == -1, '-', self.numbers)) #TODO некрасиво
        #self.numbers = arr
        print(self.arr[:9])
        print(self.arr[9:18])
        print(self.arr[18:29])
        print(f'************************************')
        #print(str(arr[:9]).)
    def strike_out_computer(self,value):
        arr = np.where(self.numbers == value, -1, self.numbers)
        self.numbers = arr
    def strike_out_user(self,value,answer):
        arr = np.where(self.numbers == value, -1, self.numbers)
        if sum(self.numbers) == sum(arr):
            #print ('False')
            self.good_answer = False
        else:
            #print('True')
            self.good_answer = True
        if answer != self.good_answer:
            self.in_game = False
        self.numbers = arr
    def check_win_card(self):
        if np.sum(self.numbers) == -15:
            self.win = True
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


















