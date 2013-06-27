Test-driven development (TDD) of the Fibonacci series.  In the first
part of each phase (1: one, 2: zero, 3: natural, 4: other), we extend
the tests to be more robust.  Then we improve the implementation until
the tests pass.  Repeat as needed ;).

    $ cd 1.1.one                   # add some tests
    $ nosetests test_fibonacci.py  # fails
    $ cd ../1.2.one                # add an implemenation
    $ nosetests test_fibonacci.py  # passes
    $ cd ../2.1.zero               # add better testing
    $ nosetests test_fibonacci.py  # fails
    …
