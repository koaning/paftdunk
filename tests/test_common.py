from paftdunk.common import counting_window


def test_window():
    res = list(counting_window([1, 2, 3, 4]))
    assert res[0] == (1, 2)
    assert res[1] == (2, 1)
    assert res[2] == (2, 3)
    assert res[3] == (3, 2)
    assert res[4] == (3, 4)
    assert res[5] == (4, 3)
