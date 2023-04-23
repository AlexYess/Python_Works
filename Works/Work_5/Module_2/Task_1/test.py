import pytest
import random
from bucketsort import bucketsort


@pytest.fixture
def random_array():
    return [random.randint(0, 10) for _ in range(10)]


def test_bucketsort(random_array):
    sorted_arr = bucketsort(random_array, 11)
    assert sorted_arr == sorted(random_array)


@pytest.mark.parametrize("k", [5, 10, 15])
def test_bucketsort_param(random_array, k):
    sorted_arr = bucketsort(random_array, k)
    assert sorted_arr == sorted(random_array)
