import pytest
from utils.other import other_function


def test_other_function(capfd):
    other_function()
    out, err = capfd.readouterr()
    assert out == "Other function.\n"
