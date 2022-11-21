import pytest
# pytest module importing done.
# account = ma
# checking = CK

from account import *  # importing account


def test_init():
    # test for init

    ma = account("try")  # mouthed to account
    assert ma.getbalance() == 0  # balance CK
    assert ma.getname() == "try"  # name CK


def test_deposit():
    # test for deposit

    ma = account("try")  # mouthed to account
    assert ma.deposit(30)
    assert ma.getbalance() == 30  # balance CK
    assert ma.deposit(0) 
    assert ma.deposit(-70)  # -70


def test_withdraw():
    # test for withdraw

    ma = account("try")  # mouthed to account
    assert ma.deposit(100)  # 100
    assert ma.withdraw(-50)  # -50
    assert ma.withdraw(50)  # 50
    assert ma.withdraw(-30)  # -30
    assert ma.withdraw(20)  # 20
    assert ma.withdraw != 0  # can't go to 0
    assert ma.getbalance() == 90  # balance CK 90
