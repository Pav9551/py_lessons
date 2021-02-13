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
    def __eq__(self, other):
        return str(self.numbers) == str(other.numbers)
    def __ne__(self, other):
        return str(self.numbers) != str(other.numbers)

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
    def __str__(self):
        return f'Содержимое карточки:{self.numbers}'
    def __len__(self):
        filt = (self.numbers > 0)
        return len(self.numbers[filt])
    def __eq__(self, other):
        return str(self.numbers) == str(other.numbers)
    def __ne__(self, other):
        return str(self.numbers) != str(other.numbers)





















