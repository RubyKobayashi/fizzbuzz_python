from fizzbuzz import FizzBuzz
import pytest


@pytest.mark.parametrize("number, expected", [
    (1, 1),
    (2, 2),
    (3, "Fizz"),
    (4, 4),
    (5, "Buzz")
])
def test_parametrize(number, expected):
     fb = FizzBuzz()
     assert fb.fizzbuzz(number) == expected
