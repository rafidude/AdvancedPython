import pytest
from utils.sum import sum_numbers, internal_function


def test_sum_numbers():
    assert sum_numbers(1, 2) == 3
    assert sum_numbers(-1, 1) == 0
    assert sum_numbers(5, 5) == 10


def test_internal_function(capfd):
    internal_function()
    out, err = capfd.readouterr()
    assert out == "This function is internal.\n"
