import numpy as np
from loto_lib import Bag,Card

def test_get_barrel():
    our_bag = Bag()
    print(our_bag)
    for i in range(100):
        print(our_bag.get_barrel())
    #последний боченок вынут несколько раз
    assert our_bag.get_barrel() == our_bag.get_barrel()
