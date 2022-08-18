# flake8: noqa
from compat_set import CompatSet


def test_empty_set():
    val = CompatSet()
    assert len(val) == 0
    assert 99 not in val
    assert None not in val
    assert "" not in val
    assert "1" not in val

    assert val == CompatSet()
    assert val != CompatSet([1])
    assert val == set()
    assert val != {1}
    assert val != dict()


def test_simple_set():
    val = CompatSet([1, 2, 3])
    assert len(val) == 3

    assert 2 in val
    assert 99 not in val
    assert None not in val
    assert "" not in val
    assert "1" not in val

    assert val == CompatSet([2, 1, 3])
    assert val == {1, 2, 3}
    assert val != {1}
    assert val != set()
    assert val != dict()


def test_difference():
    val = CompatSet([1, 2])
    dif = val.difference([2, 3])
    assert val == CompatSet([1, 2])
    assert dif == CompatSet([1])

    assert 1 in dif
    assert 2 not in dif

    assert CompatSet([1, 2]) - {2, 3} == dif
    val -= {2, 3}
    assert val == dif
    assert CompatSet([1, 2]) - set() == {1, 2}
    assert CompatSet([1, 2]) - {1} == {2}


def test_intersection():
    val = CompatSet([1, 2])
    dif = val.intersection([2, 3])
    assert val == CompatSet([1, 2])
    assert dif == CompatSet([2])

    assert 2 in dif
    assert 1 not in dif

    assert CompatSet([1, 2]) & {2, 3} == dif
    val = CompatSet([1, 2])
    val &= {2, 3}
    assert val == dif


def test_isdisjoint():
    val = CompatSet([1, 2])
    assert val.isdisjoint(set())
    assert val.isdisjoint({3})
    assert not val.isdisjoint({2, 3})


def test_issubset():
    val = CompatSet([1, 2])
    assert val.issubset({1, 2, 3})
    assert val.issubset({1, 2})
    assert not val.issubset({1})
    assert not val.issubset(set())
    assert CompatSet().issubset({1})


def test_issuperset():
    val = CompatSet([1, 2])
    assert val.issuperset(set())
    assert val.issuperset({1})
    assert val.issuperset({1, 2})
    assert not val.issuperset({1, 2, 3})
    assert CompatSet().issuperset(set())
    assert not CompatSet().issuperset({1})


def test_symmetric_difference():
    val = CompatSet([1, 2])
    dif = val.symmetric_difference([2, 3])
    assert val == CompatSet([1, 2])
    assert dif == CompatSet([1, 3])

    assert 1 in dif
    assert 2 not in dif

    assert CompatSet([1, 2]) ^ {2, 3} == dif
    val ^= {2, 3}
    assert val == dif
    assert CompatSet([1, 2]) ^ set() == {1, 2}
    assert CompatSet([1, 2]) ^ {1} == {2}


def test_update():
    val = CompatSet([1, 2])
    assert 2 in val
    assert 3 not in val
    val.update([3, 4])
    assert 3 in val
    assert 2 in val
    assert 99 not in val

    assert CompatSet([1, 2]) | {3} == {1, 2, 3}
    val = CompatSet([1, 2])
    val |= {3}
    assert val == {1, 2, 3}


def test_update_order():
    val = CompatSet([1, 7, 6, 5])
    assert list(val) == [1, 5, 6, 7]
    val.update([9])
    assert list(val) == [1, 9, 5, 6, 7]
    val.update([8])
    assert list(val) == [1, 5, 6, 7, 8, 9]


def test_difference_order():
    val = CompatSet([5, 6, 8, 9, 10, 11, 12]).difference([])
    assert list(val) == [5, 6, 8, 9, 10, 11, 12]
    val.update([16])
    assert list(val) == [16, 5, 6, 8, 9, 10, 11, 12]

    val = CompatSet([5, 6, 8, 9, 10, 11, 12])
    assert list(val) == [5, 6, 8, 9, 10, 11, 12]
    val.update([16])
    assert list(val) == [5, 6, 8, 9, 10, 11, 12, 16]
