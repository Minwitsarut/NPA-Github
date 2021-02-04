import pytest
from router import *

def test_add_int():
    r1 = Router('Cisco', 'IOSv', 'Router1')
    r1.add_int("S0/0")
    ans1 = {"S0/0" : ['-', 'not connect to any neighbor']}
    assert r1.interface == ans1
