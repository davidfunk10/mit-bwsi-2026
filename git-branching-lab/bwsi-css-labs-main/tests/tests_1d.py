from labs.lab_1.lab_1d import two_sum


def test_basic_case():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_other_case():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_duplicate_values():
    assert two_sum([3, 3], 6) == [0, 1]


def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_zero_case():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]


def test_no_solution_returns_empty_list():
    assert two_sum([1, 2, 3], 10) == []