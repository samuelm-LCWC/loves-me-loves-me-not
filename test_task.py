import pytest
from task import loves_me

def test_1():
    assert loves_me(3) == "Loves me, Loves me not, LOVES ME"

def test_2():
    assert loves_me(6) == "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

def test_3():
    assert loves_me(1) == "LOVES ME"

def test_4():
    assert loves_me(2) == "Loves me, LOVES ME NOT"