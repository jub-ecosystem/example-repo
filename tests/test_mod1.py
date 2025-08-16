import pytest
from example_repo.mod1 import do_something,sum,main



def test_mod1_do_something():
    assert do_something()

def test_mod1_sum():
    assert sum(1,2) == 3

def test_main():
    assert main()