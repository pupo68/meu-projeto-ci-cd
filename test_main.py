import pytest
from main import calculate_sum

def test_calculate_sum_success():
    assert calculate_sum(10, 5) == 15
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(0, 0) == 0

def test_calculate_sum_type_error():
    with pytest.raises(TypeError):
        calculate_sum("1", 2)
    with pytest.raises(TypeError):
        calculate_sum(1, 2.5)
