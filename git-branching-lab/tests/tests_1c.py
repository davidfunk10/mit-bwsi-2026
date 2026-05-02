import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_standard_case():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_single_positive():
    assert max_subarray_sum([1]) == 1


def test_single_negative():
    assert max_subarray_sum([-1]) == -1


def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10


def test_all_negative():
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2


def test_with_zeroes():
    assert max_subarray_sum([0, 0, 0]) == 0


def test_large_positive_block():
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23


def test_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty."):
        max_subarray_sum([])

if __name__ == "__main__":
    pytest.main()