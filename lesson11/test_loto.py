import numpy as np
import unittest

from loto_lib import Bag,Card,zero_and_ones

def test_get_barrel():
    our_bag = Bag()
    print(our_bag)
    for i in range(100):
        print(our_bag.get_barrel())
    #последний боченок вынут несколько раз
    assert our_bag.get_barrel() == our_bag.get_barrel()
def test_zero_and_ones():
    assert sum(zero_and_ones()) == 5
class Test_loto(unittest.TestCase):
    def test_create_Bag(self):
        our_bag = Bag()
        self.assertEqual(our_bag.current_barrel, our_bag.numbers[0])
    def test_str(self):
        our_bag = Bag()
        self.assertIn('Номера бочонков по порядку вытаскивания:', str(our_bag))
    def test_len(self):
        our_bag = Bag()
        self.assertEqual(len(our_bag), 90)# 90 боченков
    def test_numbers(self):
        our_bag = Bag()
        self.assertEqual(len(our_bag.numbers), 90)# 90 боченков
    def test_bag_equal(self):
        test_bag = Bag()
        test_bag2 = Bag()
        test_bag = test_bag2
        self.assertTrue(test_bag == test_bag2)
    def test_bag_ne(self):
        test_bag = Bag()
        test_bag2 = Bag()
        self.assertTrue(test_bag != test_bag2)
    def test_create_Card(self):
        Card1 = Card("Компьютер 1")
        self.assertEqual(len(Card1.numbers), 27)  # 90 боченков
    def test_show_card(self):
        Card1 = Card("Компьютер 1")
        self.assertIn('0', str(Card1.arr))
    def test_computer(self):
        Card1 = Card("Компьютер 1")
        Card1.numbers[0] = 10
        Card1.strike_out_computer(10)
        self.assertIn(-1, Card1.numbers)
    def test_user(self):
        Card1 = Card("Игрок 1")
        Card1.numbers[0] = 10
        Card1.strike_out_user(10,True)
        self.assertIn(-1, Card1.numbers)

    def test_chek_win(self):
        # создаем мешок с боченками
        our_bag = Bag()
        # создаем карту для компьютера 1
        Card1 = Card("Компьютер 1")
        while ((Card1.win == False)):
            barrel = our_bag.get_barrel()  # тянем боченок
            Card1.strike_out_computer(barrel)  # зачеркиваем
            Card1.check_win_card()  # проверяем победителя
        self.assertTrue(Card1.win)
    def test_card_str(self):
        Card1 = Card("Компьютер 1")
        self.assertIn('Содержимое карточки:', str(Card1))
    def test_card_len(self):
        Card1 = Card("Компьютер 1")
        self.assertEqual(len(Card1), 15)# 15 значений не зачеркнуто
    def test_card_equal(self):
        Card1 = Card("Компьютер 1")
        Card2 = Card("Компьютер 2")
        Card1 = Card2
        self.assertTrue(Card1 == Card2)
    def test_card_ne(self):
        Card1 = Card("Компьютер 1")
        Card2 = Card("Компьютер 2")
        self.assertTrue(Card1 != Card2)





















