import pytest
from src.iterable.get_first import get_first
from src.iterable.skip_item import skip_item
from src.iterable.get_remains import get_remains
from src.iterable.iterate import iterate


@pytest.mark.parametrize("a, expected", [
    pytest.param(["Python", "is", "awesome"], "Python", id="1"),
])
def test_get_first(a, expected):
    assert get_first(a) == expected


@pytest.mark.parametrize("a, b, expected", [
    pytest.param(["a", "b", "c", "d", "e", "f"], 2, "c", id="2"),
])
def test_skip_item(a, b, expected):
    assert skip_item(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    pytest.param(["red", "green", "blue", "orange", "yellow"], 2, "blue\norange\nyellow", id="1"),
])
def test_get_remains(a, b, expected):
    assert get_remains(a, b) == expected


@pytest.mark.parametrize("a, expected", [
    pytest.param(["Stepik", "is", "a", "great", "platform"], "Stepik\nis\na\ngreat\nplatform\n", id="1"),
])
def test_iterate(a, expected, capsys):
    iterate(a)
    captured = capsys.readouterr()
    assert captured.out == expected
