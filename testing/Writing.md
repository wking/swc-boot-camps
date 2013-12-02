## Let's start writing a python test harness

Going to use the `unittest` framework. This has been in python since python 2.6. Create a `TestHarness.py` file and type in the following:

```
import unittests

class MyTests(unittest.TestCase):

    def test1(self):
        pass

    def test2(self):
        pass

if __name__ == '__main__':

   unittest.main()
```

A test case is defined by subclassing `unittest.TestCase`. We have defined two rather uninteresting tests. If we run this we get:

```
%run TestHarness.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

Note that we assume that we are running the script from `ipython`. Each "." represents a test that has passed. A test can:

* Pass, indicated by a `.`
* Fail, indicated by an `F`
* Terminate with an Error, indicated by an `E`, that is something went wrong like your code through a segmentation fault.

Also if you want more detail you can run your tests using the `-v` flag then you would get:

```
%run TestHarness.py -v
test1 (__main__.MyTests) ... ok
test2 (__main__.MyTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.007s

OK
```
Or you can run a single test if you wish:
```
%run TestHarness.py -v MyTests.test2
test2 (__main__.MyTests) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```
Can add code that will run before and after every test:
```
    def setUp(self):
        print "\nRunning test: ",self.id(),"\n"

    def tearDown(self):
        print "Ending test: ",self.id(),"\n"
```
So that execution would now look like:
```
%run TestHarness.py

Running test:  __main__.MyTests.test1

Ending test:  __main__.MyTests.test1

.
Running test:  __main__.MyTests.test2

Ending test:  __main__.MyTests.test2

.
----------------------------------------------------------------------
Ran 2 tests in 0.020s

OK
```
This can be useful set up the *fixtures* for your tests or you could
use it to time each test:

```
import time

logfile ="timings.txt"
...
class MyTests(unittest.TestCase):

    def setUp(self):
        fh = open(logfile,"a")
        self.startTime = time.time()
        fh.write("Test %s.\n" % (self.id()))
        fh.close()

    # Run after every test.
    def tearDown(self):
        fh = open(logfile,"a")
        t  = time.time() - self.startTime
        fh.write("Time to run test: %.3f seconds.\n" % (t))
        fh.close()
...
```
Writing to a file so as not to pollute the output. The `unittest` module comes with a number of different ways that you can check that your code is working ok, for instance:

* `assertEqual(a,b)` checks that `a == b`.
* `assertNotEqual(a,b)` checks that `a != b`.
* `assertTrue(x)` checks that `x`, a boolean, is `True`.
* `assertFalse(x)` checks that x, a boolean, is `False`.
* `assertRaises(exc,fun,*args,**kwds)` checks that `fun(*args,**kwds)` raises exception `exc`.
* `assertAlmostEqual(a,b)` checks that `round(a-b,7) == 0`
* `assertNotAlmostEqual(a,b)` checks that `round(a-b,7)!=0`

Let's make it a little more interesting. Create a new python file: `MyFunctions.py` and add a function:

```
def MySum(a,b):
    return(a+b)
```
Now we want to import this function into our test harness. Add the line at the top of `TestHarness.py`:
```
from MyFunctions import MySum
```
We can now add a test to check this works:
```
    def testMySum(self):
        self.assertEqual(MySum(1,3),4)
```     
That should have worked. What happens if we try the following?

```
    MySum("a","b")
    "ab"
```
It may well be that that is perfectly acceptable behaviour but, on the other hand, you may only want numbers to be added and not to have string concatenation. We can change the sum function accordingly:
```
def MySum(a,b)
    if(type(a) == str or type(b) == str):
       raise TypeError("Can only have integers or floats")
    return(a+b)
```
We can also add a test to ensure that an exception is being raised:
```
    from MyFunctions import MyRepeatedSum
     ...
    def testMySumExceptionArg1(self):
        self.assertRaises(TypeError,MySum,1,"a")

    def testMySumExceptionArg2(self):
        self.assertRaises(TypeError,MySum,"a",2)
```
We can keep on playing these games and add further tests for `MySum` but let's define a new function:
```
def MyRepeatedSum(num,repeat):
    """
    Sums num a number of times specified by repeat.
    """
    tot = 0
    for i in range(repeat):
        tot += num
    return tot
```
Now lets import that into our test routine and do a couple of new tests:
```
    def testMyRepeatedSum1(self):
        self.assertEqual(MyRepeatedSum(1,100),100)

    def testMyRepeatedSum2(self):
        self.assertEqual(MyRepeatedSum(0.1,100),10.0)
```
When we run this we can see that we have a test failure:
```
..F...
======================================================================
FAIL: testMyRepeatedSum2 (__main__.MyTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestHarness.py", line 26, in testMyRepeatedSum2
    self.assertEqual(MyRepeatedSum(0.1,100),10.0)
AssertionError: 9.99999999999998 != 10.0

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED (failures=1)
```
We have our first test failure. You should ***never*** test for equality (`==`) or inequality (`!=`) with floating numbers due to round off errors (amongst other things). We should instead use:

```
    def testMyRepeatedSum2(self):
         NumDecPlaces = 3 # default is 7
        self.assertAlmostEqual(MyRepeatedSum(0.1,100),10.0,NumDecPlaces)
```
Now all tests should pass:
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```
This then forms the basics of how one might go on to develop a test framework using Python. We shall come back to this later but lets have a look at `nosetests`.

## `nose` - a Python test framework

`nose` is a test framework for Python that will automatically find, run and report on tests written in Python. It is an example of what has been termed an *[xUnit test framework](http://en.wikipedia.org/wiki/XUnit)*, perhaps the most famous being JUnit for Java.

To use `nose`, we write test functions, as we' have been doing, with the prefix `test_` and put these in files, likewise prefixed by `test_`. The prefixes `Test-`, `Test_` and `test-` can also be used (in fact anything that matches the regular expression ` (?:^|[b_.-])[Tt]est)`).

To run `nose` for our tests, all we have to do is type:

```
$ nosetests
```
It will find the tests and return:
```
test2 (TestHarness.MyTests) ... ok
testMyRepeatedSum1 (TestHarness.MyTests) ... ok
testMyRepeatedSum2 (TestHarness.MyTests) ... ok
testMySum (TestHarness.MyTests) ... ok
testMySumExceptionArg1 (TestHarness.MyTests) ... ok
testMySumExceptionArg2 (TestHarness.MyTests) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.233s

OK
```
As before each `.` corresponds to a successful test. 

nosetests can output an "xUnit" test report,

```
$ nosetests --with-xunit TestHarness.py
$ more nosetests.xml
```

This is a standard format that that is supported by a number of xUnit frameworks which can then be converted to HTML and presented online. 

`nose` defines additional functions which can be used to check for a rich range of conditions, e.g.

```
$ python
>>> from nose.tools import *

>>> expected = 123
>>> actual = 123
>>> assert_equal(expected, actual)
>>> actual = 456
>>> assert_equal(expected, actual)
>>> expected = "GATTACCA"
>>> actual = ["GATC", "GATTACCA"]
>>> assert_true(expected in actual)
>>> assert_false(expected in actual)
```

We can add more information to the failure messages by providing additional string arguments, e.g.

```
>>> assert_true("GTA" in actual, "Expected value was not in the output list")
```

The nodetests provide a powerful framework to write and run tests with. The only down-side is that it requires to be installed in the system you wish to run your tests on and you will require special privileges to do this or you can install locally and then set-up accordingly.

## Writing more tests - revisiting Lotka-Volterra

