import pytest
from src.aggregation.has_negative import has_negative



@pytest.mark.parametrize("s, expected", [
    pytest.param("10 5 -3 15 8", True, id="1")
])
def test_has_negative(s, expected):
    assert has_negative(s) == expected

