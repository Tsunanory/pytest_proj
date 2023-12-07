from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([2, 11, 9], 3, "test") == "test"

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 3, 9], 1) == [2, 3, 3, 9]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 1, 3], 2) == [3]
    assert arrs.my_slice([1, 1, 3, '2', 1], 3) == ['2', 1]
    assert arrs.my_slice([1, 1, 3], 1) == [1, 3]
    assert arrs.my_slice([1, 1, [2, 3], 3], 2, 3) == [[2, 3]]
    assert arrs.my_slice([1, 1, [2, 0], 3], None, -1) == [1, 1, [2, 0]]
    assert arrs.my_slice([1, 1, [2, 12], 3], 2, 3) == [[2, 12]]