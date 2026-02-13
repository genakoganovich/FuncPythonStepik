import pytest
from src.filter.filter_even import filter_even
from src.filter.filter_long_words import filter_long_words
from src.filter.filter_none import filter_none
from src.filter.filter_palindrome import filter_palindrome
from src.filter.filter_range import filter_range

@pytest.mark.parametrize("s, expected", [
    pytest.param("1 2 3 4 5 6 7 8", [2, 4, 6, 8], id="1"),
])
def test_filter_even(s, expected):
    assert filter_even(s) == expected

@pytest.mark.parametrize("s, expected", [
    pytest.param("map filter zip enumerate python", ['filter', 'enumerate', 'python'], id="1"),
])
def test_filter_long_words(s, expected):
    assert filter_long_words(s) == expected

@pytest.mark.parametrize("s, expected", [
    pytest.param("apple,,banana,cherry,", ['apple', 'banana', 'cherry'], id="1")
])
def test_filter_none(s, expected):
    assert filter_none(s) == expected

@pytest.mark.parametrize("s, expected", [
    pytest.param("level rotator hello world radar kayak", ['level', 'rotator', 'radar', 'kayak'], id="1")
])
def test_filter_palindrome(s, expected):
    assert filter_palindrome(s) == expected


@pytest.mark.parametrize("s, lower_bound, upper_bound, expected", [
    pytest.param("10 5 25 3 40 18 9", 10, 30, [10, 25, 18], id="1")
])
def test_filter_range(s, lower_bound, upper_bound, expected):
    assert filter_range(s, lower_bound, upper_bound) == expected