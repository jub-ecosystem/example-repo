import pytest
from exmaple_repo.mod1 import do_something,sum



def test_mod1_do_something():
    assert do_something()

def test_mod1_sum():
    assert sum(1,2) == 3

def main():
    return False