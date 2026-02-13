import pytest
from src.map.add_product import add_product
from src.map.apply_chain import apply_chain
from src.map.get_first_letter import get_first_letter
from src.map.get_total_cost import get_total_cost
from src.map.map_str_to_int import map_str_to_int_list

@pytest.mark.parametrize("s, expected", [
    pytest.param("1 5 10 25", [1, 5, 10, 25], id="1"),
])
def test_map_str_to_int_list(s, expected):
    assert map_str_to_int_list(s) == expected


@pytest.mark.parametrize("s, expected", [
    pytest.param("apple, banana, cherry", ['product: apple', 'product: banana', 'product: cherry'], id="1"),
])
def test_add_product(s, expected):
    assert add_product(s) == expected


@pytest.mark.parametrize("s, expected", [
    pytest.param("Python function map", ['P', 'F', 'M'], id="1"),
])
def test_get_first_letter(s, expected):
    assert get_first_letter(s) == expected

@pytest.mark.parametrize("s, expected", [
    pytest.param("10.9 3.14 25.5 99.8", ['11', '3', '26', '100'], id="1"),
])
def test_apply_chain(s, expected):
    assert apply_chain(s) == expected

@pytest.mark.parametrize("s, t, expected", [
    pytest.param("100 20 50", "3 5 2", [300, 100, 100], id="1"),
])
def test_get_total_cost(s, t, expected):
    assert get_total_cost(s, t) == expected