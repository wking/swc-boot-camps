# Writing tests for `mean()`

There are a few tests for the `mean()` function.  What are some tests
that should fail?  Add at least three test cases to this set.  Edit
the `test_mean.py` file which tests the `mean()` function in
`mean.py`.

*Hint:* Think about what form your input could take and what you should
do to handle it. Also, think about the type of the elements in the list.
What should be done if you pass a list of integers? What if you pass a
list of strings?

 You can test a particular implementation by using `PYTHONPATH`:

    $ PYTHONPATH=basic nosetests test_mean.py
    $ PYTHONPATH=exceptions nosetests test_mean.py
