# Test locations

Nose [looks in the usual places][finding-tests].

* Nose tests live in files matching `[Tt]est[-_]`
* Nose can find `unittest.TestCase` subclasses.
* Nose also finds functions matching the `testMatch` regular
  expression.

# Test syntax

Nose tests use assertions

```python
assert should_be_true()
assert not should_not_be_true()
```

There are lots of assertion helpers in `nose.tools`
([docs][nose-assertions]), which [exports][nose-assertion-export] the
[unittest assertions][unittest-assertions] in [PEP 8][pep8] syntax
(`assert_equal` rather than `assertEqual`).  There are more assertion
helpers in `numpy.testing` ([docs][NumPy-assertions]) for arrays and
numerical comparisons.

# Basic nose

Writing tests for `mean()`:

* Basic implementation: [mean.py][basic-mean]
* Internal exception catching: [mean.py][exception-mean]
* Embedded tests: [mean.py][embedded-test-mean]
* Independent tests: [test_mean.py][test-mean]

# Test-driven development

We have [a Fibonacci example][fibonacci] with a series of increasingly
detailed tests and implementations.

# Quality assurance

Can you think of other tests to make for the Fibonacci function?  I
promise there are at least two.

Implement one new test in `test_fibonacci.py`, run `nosetests`, and if
it fails, implement a more robust function for that case.


[finding-tests]: https://nose.readthedocs.org/en/latest/finding_tests.html
[nose-assertions]: https://nose.readthedocs.org/en/latest/testing_tools.html#testing-tools
[nose-assertion-export]: https://github.com/nose-devs/nose/blob/master/nose/tools/trivial.py#L33
[unittest-assertions]: http://docs.python.org/2/library/unittest.html#assert-methods
[pep8]: http://www.python.org/dev/peps/pep-0008/
[NumPy-assertions]: http://docs.scipy.org/doc/numpy/reference/routines.testing.html#asserts
[basic-mean]: exercises/mean/basic/mean.py
[exception-mean]: exercises/mean/exceptions/mean.py
[embedded-test-mean]: exercises/embedded-tests/mean.py
[test-mean]: exercises/test_mean.py
[fibonacci]: exercises/fibonacci
