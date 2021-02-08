import pytest

import math


def test_filter():
    test_list = [1, 7, 4, -5, 3]
    result_list = [1, 7, 4, 3]
    assert list(filter(lambda y: True if y > 0 else False, test_list)) == result_list

def test_map():
    values = [-2, -1, 0, 1, 2]
    result = [-4, -2, 0, 2, 4]
    assert list(map(lambda y: y*2, values)) == result

def test_sorted():
    values = [1, 5, 8, -9, 13]
    result = [-9, 1, 5, 8, 13]
    assert sorted(values) == result

def test_pi():
    assert round(math.pi, 2) == 3.14

def test_sqrt():
    values = [0, 1, 4, 9, 16, 25]
    result = [0, 1, 2, 3, 4, 5]
    assert list(map(lambda y: math.sqrt(y), values)) == result

def test_pow():
    values = [0, 1, 2, 3, 4, 5]
    result = [0, 1, 4, 9, 16, 25]
    assert list(map(lambda y: math.pow(y,2), values)) == result

def test_hypot():
    a = [1.00, 2.00, 3.00, 4.00, 5.00]
    b = [4.00, 4.00, 4.00, 4.00, 4.00]
    c = [4.12, 4.47, 5.00, 5.66, 6.40]
    res = list(zip(a, b))
    assert list(map(lambda y: round(math.hypot(*y), 2), res)) == c


