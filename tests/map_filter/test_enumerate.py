import pytest
from src.zip_enumerate.enumerate_tasks import enumerate_tasks
from src.zip_enumerate.create_dict import create_dict
from src.zip_enumerate.enumerate_even_position import enumerate_even_position
from src.zip_enumerate.sum_mult import sum_mult
from src.zip_enumerate.combine_output import combine_output



@pytest.mark.parametrize("s, expected", [
    pytest.param("Помыть посуду,Выучить Python,Сделать зарядку",
                 "1. Помыть посуду\n2. Выучить Python\n3. Сделать зарядку",
                 id="1"),
])
def test_enumerate_tasks(s, expected):
    assert enumerate_tasks(s) == expected


@pytest.mark.parametrize("s, t, expected", [
    pytest.param("name age city",
                 "Anna 25 Moscow",
                 {'name': 'Anna', 'age': '25', 'city': 'Moscow'},
                 id="1"),
])
def test_create_dict(s, t, expected):
    assert create_dict(s, t) == expected


@pytest.mark.parametrize("s, expected", [
    pytest.param("A B C D E F G", "A\nC\nE\nG")
])
def test_enumerate_even_position(s, expected):
    assert enumerate_even_position(s) == expected


@pytest.mark.parametrize("s, t, expected", [
    pytest.param("1 2 3", "4 5 6", 32, id="1"),
])
def test_sum_mult(s, t, expected):
    assert sum_mult(s, t) == expected

@pytest.mark.parametrize("s, t, expected", [
    pytest.param("apple,banana,bread", "50,30,25", "1. apple - 50\n2. banana - 30\n3. bread - 25", id="1"),
])
def test_combine_output(s, t, expected):
    assert combine_output(s, t) == expected