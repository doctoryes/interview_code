
import pytest
import k_window


@pytest.mark.parametrize(
    "list1,list2,k,removals_expected,list1_expected,list2_expected",
    [
        [
            [], [], 10, 0, [], []
        ],
        [
            [1, 2], [], 10, 0, [1, 2], []
        ],
        [
            [], [1, 2], 10, 0, [], [1, 2]
        ],
    ]
)
def test_lists_empty(list1, list2, k, removals_expected, list1_expected, list2_expected):
    r = k_window.unique_k_window(list1, list2, k)
    assert(r == removals_expected)
    assert(list1 == list1_expected)
    assert(list2 == list2_expected)

@pytest.mark.parametrize(
    "list1,list2,k,removals_expected,list1_expected,list2_expected",
    [
        [
            [1, 2, 3], [1, 2, 3], 1, 1, [1, 2, 3], [2, 3]
        ],
        [
            [1, 2, 3], [1, 2, 3], 0, 0, [1, 2, 3], [1, 2, 3]
        ],
        [
            [1, 2, 3], [1, 2, 3], -1, 0, [1, 2, 3], [1, 2, 3]
        ],
        [
            [1, 2, 3], [1, 2, 3], 100000, 3, [1, 2, 3], []
        ],
    ]
)
def test_k_values(list1, list2, k, removals_expected, list1_expected, list2_expected):
    r = k_window.unique_k_window(list1, list2, k)
    assert(r == removals_expected)
    assert(list1 == list1_expected)
    assert(list2 == list2_expected)

@pytest.mark.parametrize(
    "list1,list2,k,removals_expected,list1_expected,list2_expected",
    [
        [
            [1, 1, 1, 1, 1, 2], [1, 10], 2, 1, [1, 1, 1, 1, 1, 2], [10]
        ],
        [
            [1, 10], [1, 1, 1, 1, 1, 2], 2, 1, [10], [1, 1, 1, 1, 1, 2]
        ],
        [
            [1, 2, 1, 2, 1, 2, 3], [2, 1, 2, 1, 2, 1, 4],
            3, 4,
            [1, 1, 1, 2, 3], [2, 2, 2, 1, 4]
        ],
    ]
)
def test_minimal_removals(list1, list2, k, removals_expected, list1_expected, list2_expected):
    r = k_window.unique_k_window(list1, list2, k)
    assert(r == removals_expected)
    assert(list1 == list1_expected)
    assert(list2 == list2_expected)

