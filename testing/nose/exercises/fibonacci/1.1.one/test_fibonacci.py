from nose.tools import assert_equal

from fibonacci import fib


def test_fib1():
    obs = fib(2)
    exp = 1
    assert_equal(obs, exp)
