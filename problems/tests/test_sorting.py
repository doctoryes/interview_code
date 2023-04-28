
import random
import sorting

TEST_BIG_ARR_LENGTH = 500

def test_bubble_sort():
    assert(sorting.bubble_sort([4,3,2,1]) == [1,2,3,4])

def test_merge_sort():
    assert(sorting.merge_sort([4,3,2,1]) == [1,2,3,4])

def test_quick_sort():
    assert(sorting.quick_sort([4,3,2,1]) == [1,2,3,4])

def test_insertion_sort():
    assert(sorting.insertion_sort([4,3,2,1]) == [1,2,3,4])

def test_large_array_all_sorts():
    test_arr = [random.randint(1,100000) for __ in range(0, TEST_BIG_ARR_LENGTH)]
    b_arr = sorting.bubble_sort(test_arr)
    m_arr = sorting.merge_sort(test_arr)
    q_arr = sorting.quick_sort(test_arr)
    i_arr = sorting.insertion_sort(test_arr)
    assert(b_arr == m_arr)
    assert(m_arr == q_arr)
    assert(q_arr == i_arr)
