"""test the kata exercise"""
from exercise import exercise


def test1():
    assert exercise(0, 1, 2) == 2


def test2():
    assert exercise(0, 1, 3) == 3


def test3():
    assert exercise(0, 1, 5) == 8


def test4():
    assert exercise(0, 1, 8) == 34


def test5():
    assert exercise(0, 1, 1) == 1


def test6():
    assert exercise(0, 1, 0) == 1


def test7():
    assert exercise(2, 3, 3) == 13
