# flake8: noqa
from compat_set import CompatSet


def test_empty_contains():
    val = CompatSet()
    assert 99 not in val
    assert None not in val
    assert "" not in val
    assert "1" not in val


def test_new_contains():
    val = CompatSet([1, 2, 3])
    assert 2 in val
    assert 99 not in val
    assert None not in val
    assert "" not in val
    assert "1" not in val


def test_empty_eq():
    val = CompatSet()
    assert val == CompatSet()
    assert val != CompatSet([1])


def test_new_eq():
    assert CompatSet([1, 2]) == CompatSet([2, 1])


def test_difference():
    val = CompatSet([1, 2])
    dif = val.difference([2, 3])
    assert val == CompatSet([1, 2])
    assert dif == CompatSet([1])
    assert 1 in dif
    assert 2 not in dif
    assert val - [2, 3] == dif
    val -= [2, 3]
    assert val == dif


def test_intersection():
    val = CompatSet([1, 2])
    dif = val.intersection([2, 3])
    assert val == CompatSet([1, 2])
    assert dif == CompatSet([2])
    assert 2 in dif
    assert 1 not in dif

    assert CompatSet([1, 2]) & [2, 3] == CompatSet([2])
    val = CompatSet([1, 2])
    val &= [2, 3]
    assert val == CompatSet([2])


def test_update():
    val = CompatSet([1, 2])
    assert 2 in val
    assert 3 not in val
    val.update([3, 4])
    assert 3 in val
    assert 2 in val
    assert 99 not in val

    assert CompatSet([1, 2]) | [3] == CompatSet([1, 2, 3])
    val = CompatSet([1, 2])
    val |= [3]
    assert val == CompatSet([1, 2, 3])


def test_update_order():
    val = CompatSet([1, 7, 6, 5])
    assert list(val) == [1, 5, 6, 7]
    val.update([9])
    assert list(val) == [1, 9, 5, 6, 7]
    val.update([8])
    assert list(val) == [1, 5, 6, 7, 8, 9]
