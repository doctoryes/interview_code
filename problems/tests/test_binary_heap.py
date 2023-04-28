
import random
import pytest
import binary_heap


def test_binary_heap_insert_root():
    x = binary_heap.BinaryHeap(binary_heap.HeapType.MAX)
    x.insert(44)
    assert(x.root.value == 44)
    assert(x.root.left is None)
    assert(x.root.right is None)
    assert(x.root.parent is None)

@pytest.mark.parametrize(
    "type,expected",
    [
        [
            binary_heap.HeapType.MAX, 1134
        ],
        [
            binary_heap.HeapType.MIN, 4
        ],
    ]
)
def test_binary_heap_insert_multilevel(type, expected):
    x = binary_heap.BinaryHeap(type)
    x.insert(11)
    x.insert(22)
    x.insert(33)
    x.insert(4)
    x.insert(55)
    x.insert(1001)
    x.insert(6)
    x.insert(777)
    x.insert(88)
    x.insert(99)
    x.insert(1134)
    assert(x.root.value == expected)
    assert(x.root.parent is None)
    assert(x.root.left is not None)
    assert(x.root.right is not None)

@pytest.mark.parametrize(
    "type,expected",
    [
        [
            binary_heap.HeapType.MAX, 10001
        ],
        [
            binary_heap.HeapType.MIN, -4
        ],
    ]
)
def test_binary_heap_insert_lots(type, expected):
    x = binary_heap.BinaryHeap(type)
    for __ in range(0, 1000):
        x.insert(random.randint(1,5000))
    x.insert(expected)
    # Ensure the correct value has bubbled to the top.
    assert(x.root.value == expected)
