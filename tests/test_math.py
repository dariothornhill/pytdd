import pytest
from src.math import sub, add, mul, Math


# a simple test
def test_sub():
    assert sub(2, 1) == 1


# marking

# mark test as skipped
@pytest.mark.skip
def test_pow():
    assert pow(2, 3) == 8

# mark test as expected to fail, produces xfail denoted by x


@pytest.mark.xfail
def test_xsub():
    assert sub(2, 1) == 2

# if a test is expectd to fail but passes it produces an xpass deonted by X


@pytest.mark.xfail
def test_xpasssub():
    assert sub(2, 1) == 1

# marking as parameterized fixture, similar to data provider in phpUnit


@pytest.mark.parametrize("test_input,expected", [
    ([3, 5], 8),
    ([2, 4], 6),
    ([6, 9], 15),
    ([0, 0], 0),
    ([1, 0], 1),
    ([1, 1], 2),
    ([1, 2], 3),
    ([-1, 0], -1),
    ([-1, -1], -2),
])
def test_add(test_input, expected):
    assert add(test_input[0], test_input[1]) == expected

# parameterized fixture, similar to data provider in phpUnit


@pytest.mark.parametrize("test_input,expected", [
    ([3, 5], 15),
    ([2, 4], 8),
    ([6, 9], 54),
    ([0, 0], 0),
    ([1, 0], 0),
    ([1, 1], 1),
    ([1, 2], 2),
    ([-1, 0], 0),
    ([-1, -1], 1),
])
def test_mul(test_input, expected):
    assert mul(test_input[0], test_input[1]) == expected

# exceptions


def test_mulex():
    with pytest.raises(TypeError):
        add("a", 5)

# testing class methods


def test_div():
    instance = Math()
    assert instance.div(2, 1) == 2

# dependency injection

# mocking, spying etc
