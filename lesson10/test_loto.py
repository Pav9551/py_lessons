import numpy as np
import unittest

from loto_lib import Bag,Card

def test_get_barrel():
    our_bag = Bag()
    print(our_bag)
    for i in range(100):
        print(our_bag.get_barrel())
    #последний боченок вынут несколько раз
    assert our_bag.get_barrel() == our_bag.get_barrel()
class Test_loto(unittest.TestCase):
    def test_create_Bag(self):
        our_bag = Bag()
        self.assertEqual(our_bag.current_barrel, our_bag.numbers[0])
    def test_str(self):
        our_bag = Bag()
        self.assertIn('Номера бочонков по порядку вытаскивания:', str(our_bag))
    def test_numbers(self):
        our_bag = Bag()
        self.assertEqual(len(our_bag.numbers), 90)# 90 боченков
    def test_get_barrel(self):
        our_bag = Bag()
        self.assertNotEqual(our_bag.get_barrel(), our_bag.get_barrel())
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




















