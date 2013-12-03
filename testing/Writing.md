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

Start by pulling an updated version of the scripts. In the students directory you checked out from GitHub run the following commands:

```
    git branch --track instructors remotes/origin/instructors
```

Here, you re setting a local branch to track the remote instructors branch. Now we can checkout a directory from the instructor directory to the student directory:

```
    git checkout instructors lotkavolterra
```

If you on inside the `lotkavolterra` directory you will find:

* `config.cfg`: configuration file with the prey-predator parameters.
* `lotkavolterra.png`: a png of the differential equations.
* `lotkavolterra.py`: library of simulation and plotting functions.
* `plot_lv.py`: script to read data file and plot data.
* `simplelotka.py`: what would correspond to your first version of the code.
* `simulate_and_plot_lv.py`: driving script.
* `simulate_lv.py`: script to read configuration file, run simulation and save data file.

If you run `simulate_and_plot_lv.py` you will get the a graph of the output to get a feeling for what you would expect. If you do:

```
$ python simulate_and_plot_lv.py --help
```

You can see what the possible options are. So, you could start with the defaults:

```
$ python simulate_and_plot_lv.py
```

which should be familiar. You could make an initial 0 prey population:

```
$ python simulate_and_plot_lv.py -r 0
```

and, as expected the predator population would decay to zero unless you give them a negative birth rate:

```
$python simulate_and_plot_lv.py -r 0 -c -0.1
```
Should that be allowed? Regardless, this is not a good way to test the code. Instead we want to write to file and separate the plotting process from the production of the results. This is done in:

```
$ python simulate_lv.py config.cfg output.csv
$ python plot_lv.py output.csv
```

where the first script takes a configuration script (`config.cfg`) and an output filename (`output.csv`) and the second takes the output file and plots the results. 

There are several testing approaches that can be taken. Let's assume, for now, that you are confident in the results that you are producing and want to ensure that you do not mess these up so want to generate a set of reference configuration and output files you can compare against - in essence you are creation some *regression tests*. We will iterate our way to doing a test.

First run the first script to generate the reference output that is going to be used for the tests. We want to preserve these so:

```
$ cp config.cfg Test1Config.cfg
$ cp output.csv Test1Output.csv
```

Will use the `unittest` framework as that can be used on its own and with unit tests. Call this script `TestLTKV.py`

```
import unittest

class TestLTKV(unittest.TestCase):

    def test1(self):
        pass


if __name__ == '__main__':

   unittest.main()
```

Now, we want to specify:

* What the script we are running is called
* What config file is called
* What the output files is going to be called
* What the reference file we are comparing this against is going to be called
* We want a function that will run the script to generate the output
* We want a test function that will compare the two files and return `True` if the two files are the same

So the test, essentially becomes:

```
    def test1(self):
        script  = "simulate_lv.py"
        config  = "Test1Config.cfg"
        outfile = "outputT1.csv"
        reffile = "Test1Output.csv"
        runTest(script, config, outfile)
        self.assertTrue(compareFiles(reffile,outfile))
```

Let's start by looking at the `compareFiles()` function. There is a file comparison function in Python so we can leverage off that:

```
import filecmp

def compareFiles(file1,file2):
    return filecmp.cmp(file1,file2)
```

So, that is fairly straightforward BUT is a bit naive, for instance it will NOT work if you are expecting floating point differences. In that case, you would have to employ a much more sophisticated approach where you have to inspect the
inside of each file and compare element by element showing that they are
the same within a given tolerance - to get an idea as to how you might do 
that have a look at the file [regression_test.py](http://depts.washington.edu/clawpack/users/claw/python/pyclaw/regression_test.py).

Now, let's look at how we might run the code. For this we use the `subprocess` module in Python:

```
import subprocess

def runTest(script,config,outfile):
    subprocess.call(["python",script,config,outfile])

```

So the whole script now looks like:

```
import unittest
import filecmp
import subprocess

def runTest(script,config,outfile):
    subprocess.call(["python",script,config,outfile])

def compareFiles(file1,file2):
    return filecmp.cmp(file1,file2)

class TestLTKV(unittest.TestCase):

    def test1(self):
        script  = "simulate_lv.py"
        config  = "Test1Config.cfg"
        outfile = "outputT1.csv"
        reffile = "Test1Output.csv"
        runTest(script, config, outfile)
        self.assertTrue(compareFiles(reffile,outfile))


if __name__ == '__main__':

   unittest.main()
```

So let's run the script:

```
python TestLTKV.py
F
======================================================================
FAIL: test1 (__main__.TestLTKV)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestLTKV.py", line 19, in test1
    self.assertTrue(compareFiles(reffile,outfile))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.608s

FAILED (failures=1)
```

Oops, what happened there? If you do a `diff` between the two files you get:

```
diff Test1Output.csv outputT1.csv
2c2
< # Produced by simulate_lv.py on Mon Dec 02 15:32:34 2013
---
> # Produced by simulate_lv.py on Mon Dec 02 17:23:51 2013
```

The temptation here is to go back into the script and comment out the line that is producing the comment however this is not good practice as having that kind of provenance in your data can prove invaluable. We will just have to work a little harder in our comparison function.

Basically we want to look at a line by line comparison but ignore the remaining parts of any lines that have a `#` in them. Let's try a new version. What we want is:

```
def compareFiles(file1, file2):
    # Read the contents of each file.
    # Check we have the same number of lines
      # If not return False
    # Iterate over the lines
      # Strip out any content that begins with a hash
      # Compare lines
      # If different return False
    # Return true
```

Now all we have to do is fill in the code. This gives us:

```
def compareFiles(file1,file2):

    # open each file and read in the lines
    f1 = open(file1,"r")
    lines1 = f1.readlines()
    f1.close()
    f2 = open(file2,"r")
    lines2 = f2.readlines()
    f2.close()

    # Check we have the same number of lines else the
    # files are not the same.
    if(len(lines1) != len(lines2)):
       print "File does not have the same number of lines.\n"
       return(False)

    # Now iterate over the lines
    for i in range(len(lines1)):

        # This splits the string on a '#' character, then keeps
        # everything before the split. The 1 argument makes the .split()
        # method stop after a one split; since we are just grabbing the
        # 0th substring (by indexing with [0]) you would get the same 
        # answer without the 1 argument, but this might be a little bit 
        # faster. From steveha at http://tinyurl.com/noyk727

        lines1[i] = lines1[i].split("#",1)[0]
        line1     = lines1[i].rsplit()

        lines2[i] = lines2[i].split("#",1)[0]
        line2     = lines2[i].rsplit()

        if(line1 != line2):
           print "Line ",i+1," not the same\n",file1,":",line1,"\n",file2,
           print ": ",line2,"\n"
           return False

    # Got through to here so it appears all lines are the same.
    return True
```

If we use this routine we now find that our test passes:

```
python TestLTKV.py
.
----------------------------------------------------------------------
Ran 1 test in 0.610s

OK
```

But now we have a paradigm that we can use for multiple different number
of configuration files and output files. 

Now time for you to try and write some tests. You could try to ensure
that if the initial conditions for the prey is set to zero, the predator
numbers will decay to zero or try testing some other feature of the trial
scripts. You will find that you will deepen your understanding of the code
by doing these tests.

In essence too you will see  that you can use Python as a test harness for non-Python codes as well - in this case we used a Python script but you could have based it on a C or Fortran executable. In that case though you may have to 
look at individual elements, element by element if you are using floating point values.

Previous: [Testing](README.md) Next: [Testing in practice](RealWorld.md)