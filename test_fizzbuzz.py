from fizzbuzz import FizzBuzz
import pytest


@pytest.mark.parametrize("number, expected", [
    (1, 1),
    (2, 2),
])
def test_parametrize(number, expected):
     fb = FizzBuzz()
     assert fb.fizzbuzz(number) == expected
