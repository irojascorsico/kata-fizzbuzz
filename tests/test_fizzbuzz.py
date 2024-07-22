import pytest
from fizzbuzz import FizzBuzz

@pytest.mark.parametrize("number, expected_result", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz")
])
def test_fizzbuzz(number, expected_result):
    my_fizzbuzz = FizzBuzz(number)
    assert my_fizzbuzz.convert_to_fizzbuzz() == expected_result