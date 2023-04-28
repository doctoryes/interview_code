
import pytest
from binary_search import BinarySearch

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        [
            [-5,0,3,5,9,12], 12, 5
        ],
        [
            [-5,0,3,5,9,12], -5, 0
        ],
        [
            [-5,0,3,5,9,12], 44, -1
        ],
        [
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811],
            10946, 21
        ],
    ]
)
def test_binary_search(nums, target, expected):
    bs = BinarySearch()
    assert(bs.search(nums, target) == expected)


