import pytest
from router import *


def test_add_int():
    r1 = Router('Cisco', 'IOSv', 'R1')
    r2 = Router('Cisco', '3745', 'R2')
    r3 = Router('Juniper', 'MXS', 'R3')
    r1.add_int("S0/0")
    r2.add_int("S0/3")
    r3.add_int("S0/0")
    ans1 = {"S0/0": ['-', 'not connect to any neighbor']}
    ans2 = {"S0/3": ['-', 'not connect to any neighbor']}
    ans3 = {"S0/0": ['-', 'not connect to any neighbor']}
    assert r1.interface == ans1
    assert r2.interface == ans2
    assert r3.interface == ans3
