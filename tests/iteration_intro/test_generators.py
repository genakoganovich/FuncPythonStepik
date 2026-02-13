import pytest
import random
from src.generators.countdown import countdown
from src.generators.powers_of_two import powers_of_two
from src.generators.random_numbers import random_numbers
from src.generators.get_len import get_len
from src.generators.sum_square_even import sum_square_even


@pytest.mark.parametrize('n, expected',[
    pytest.param(5, [5, 4, 3, 2, 1], id="n = 5"),
    pytest.param(1, [1], id="n = 1"),
    pytest.param(0, [], id="n = 0"),
])
def test_countdown(n, expected):
    assert list(countdown(n)) == expected


@pytest.mark.parametrize('n, expected', [
    pytest.param(4, [1, 2, 4, 8, 16], id="n = 4"),
    pytest.param(0, [1], id="n = 0"),
    pytest.param(1, [1, 2], id="n = 1"),
])
def test_powers_of_two(n, expected):
    assert list(powers_of_two(n)) == expected


@pytest.mark.parametrize('count, limit, expected', [
    pytest.param(5, 100, [82, 15, 4, 95, 36], id="count = 5, limit = 100"),
    pytest.param(0, 0, [], id="count = 0, limit = 0"),
])
def test_random_numbers(count, limit, expected):
    random.seed(42)
    assert list(random_numbers(count, limit)) == expected


@pytest.mark.parametrize('s, expected', [
    pytest.param("map filter zip enumerate", [3, 6, 3, 9], id="1"),
])
def test_get_len(s, expected):
    assert list(get_len(s)) == expected

@pytest.mark.parametrize('s, expected', [
    pytest.param("1 2 3 4 5 6", 56, id="1"),
])
def test_sum_square_even(s, expected):
    assert sum_square_even(s) == expected