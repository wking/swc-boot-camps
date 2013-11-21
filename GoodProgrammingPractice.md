
# Good Programming Practice

Yesterday, we finished with a script that simulated predator-prey
behavior via an implementation of the Lotka-Volterra equations using
NumPy, SciPy and matplotlib.  

Today we'll clean up that script into a program, exploring aspects of
good programming practice along the way. 

## Pull up the `import` statements

First, we will pull our `import` statements up to the top of our file.

    import numpy as np
    from matplotlib import pyplot as plt
    from scipy import integrate

This conforms to the advice in [PEP 8 -- Style Guide for Python
Code](http://www.python.org/dev/peps/pep-0008/). Many languages have
style guides which specify conventions as to how constants, variables
and functions should be named, how code should be indented, what types
of code goes where etc. These are designed to help us produce readable
code that is understandable by others. By conforming to a style guide,
we are being consistent, so that once someone has learned the style
for a particular language,they can more readily recognise what parts
of the code does what, regardless of who wrote the code - providing
they conformed to the style guide.

While code is ultimately destined to be processed by a computer, it is
humans that spend a significant amount of time reading and writing it,
and your time is more valuable than computer time, so anything that
makes the job of reading and writing code easier is a good thing!

Now, we run our script to see that it still works.

## Convert into functions

Our program consists of two main parts, that which does the
computation, and that which plots the results. We can pull out the
code that does the computation into a new function:

    def simulate():
        t = np.linspace(0, 20, 2000)
        X_initial = np.array([20, 4])
        X = integrate.odeint(dX_dt, X_initial, t)
        prey = X[:, 0]
        predators = X[:, 1]
        return (t, prey, predators)

As it's a function, we now need to return the time series and the
predator and prey populations at each time-step. We return these as a
2 element tuple. 

Likewise, we can pull out the code that plots the results into a new
function.  

    def plot(t, prey, predators):
        fig = plt.figure()
        plt.plot(t, prey, 'r-', label='Prey')
        plt.plot(t, predators, 'b-', label='Predators')
        plt.grid()
        plt.legend(loc='best')
        plt.xlabel('time')
        plt.ylabel('population')
        plt.title('Evolution of predator and prey populations')
        plt.show()

Finally, we need to add a bit of 'glue':

    (t, prey, predators) =  simulate()
    plot(t, prey, predators)

We now run this to see that it still works.

## Remove dependence on global variables

We have a number of variables that are global, they are used within
our functions but are assumed to have been defined elsewhere. Global
variables can be a problem for many reasons. One of these is that it
hinders our ability to understand code - given one of our functions we
then have to root around looking for where the global variables are
defined to see what value they might be.

We'll start with `dX_dt. Let's add arguments to the function, so we
know, when looking at the function body, where those values come from:

    def dX_dt(X, t, a, b, c, d):
        return np.array([ a*X[0] - b*X[0]*X[1] , -c*X[1] + d*b*X[0]*X[1] ])

Now we need to change the call to this function:

    X = integrate.odeint(dX_dt, X_initial, t, args=(a, b, c, d))

We use this `args` notation here as a consequence of how `odeint` is
defined. `odeint` unpacks `args` and passes them to `dX_dt` as a
conventional function call.

We now run this to see that it still works.

Now, let's do the same for `simulate`.

## Remove hard-coded values

We have hard-coded values for the initial populations of prey and
predators and the number of time-steps and the end-time. Hard-coded
values are a problem - if we wanted to change the number of time steps
or end time we'd have to edit our function, so let's pass those in as
arguments too. Define the initial values for these at the top of the
file.

## Refactor into a module

We now have a single script that consists of functions and code that
is executed directly. We may want to use these functions in other
scripts, so we can pull them out into a library.

Create a new file, `lotkavolterra.py`, and copy the `import`
statements and the functions into it.

Now remove the functions and redundant `import` statements from your
script and run it again.

We get an error as our functions are now defined outside our
script. We need to import them:

    from lotkavolterra import simulate
    from lotkavolterra import plot

If we run it again it should still work.

## Rename variables

Our variable and function names in lotkavolterra.py are somewhat
cryptic. Readable variable names help our code to be
self-documenting. So, let's rename:

* `dX_dt` - update predator and prey populations
* `X` - predator and prey populations
* `t` (in `dX_dt`) - time step
* `t` (in `simulate`) - time series

We'll deal with the rest shortly.

## Abstract out related variables into a data structure

The argument list to `simulate` is getting rather big - it has 8
arguments - which can impact upon readability. We can reduce the
number of arguments by recognising that the arguments group into those
for prey and those for prey, plus the end time and time-series.

Let's use a Python dictionary to store the configuration values for
prey and predators. A Python dictionary is a set of key-value
pairs. If we give the dictionary a key, we get back the associated
value. Dictionaries are similar to associative arrays or hashtables in
other languages.

Let us first define some keys in `lotkavolterra.py`:

    BIRTH = "birth"
    DEATH = "death"
    POPULATION = "population"

In your script, import these keys:

    from lotkavolterra import BIRTH
    from lotkavolterra import DEATH  
    from lotkavolterra import POPULATION

Then create two dictionaries:

    prey_config = {}
    predator_config = {}

Now, 

* Update your script to populate the dictionaries e.g.

    prey_config[BIRTH] = a

* Update `simulate` and `dX_dt` to replace the 6 arguments relating to
prey and predators with two arguments, `prey_config` and `predator_config`.

* Update `dX_dt` to pull out values from the dictionaries e.g.

    prey_config[BIRTH]

If you get stuck as someone sitting by you - a fresh pair of eyes on
code can work wonders.

What we know about software development - code reviews work. Fagan
(1976) discovered that a rigorous inspection can remove 60-90% of
errors before the first test is run. M.E., Fagan (1976). [Design and
Code inspections to reduce errors in program
development](http://www.mfagan.com/pdfs/ibmfagan.pdf). IBM Systems
Journal 15 (3): pp. 182-211. 

Similarly, we currently return a tuple from `simulate`. It could be
good if we could return a NumPy array that contained our time-steps
plus the prey and predator populations at each time-step. The array
returned by `integrate.odeint` already contains the prey and predator
populations at each time-step, and we have each time-step in the array
returned by `np.linspace` so we can insert the time-steps as a first
column by doing:

    data = np.insert(populations, 0, time_series, axis=1)

As this may be a bit cryptic to someone not familiar with NumPy we can
add a comment:

    # Insert time_series as a new first column.

Comments in-code should be used sparingly, to tell us why the code as
it is and also to make something which may be confusing, clear.

This inserts `time_series` into `populations` at index 0 of the 1st
axis (as our data is 2D it inserts `time_series` as a new first
column). We can now just return this instead of a tuple and remove
the, now redundant, lines:

    prey = X[:, 0]
    predators = X[:, 1]

We now need to change `plot` to take in a single argument and then
unpack the data. To unpack the data we can use:

* Time series - `data[:,0]`
* Prey values - `data[:,1]`
* Predator values - `data[:,1]`

Finally, we need to change our script to reflect the fact that
`simulate` returns a single array and `plot` takes in a single array. 

## Save data as a file

So, we now have a program that runs the Lotka-Volterra equations to
determine the evoluation of prey and predators over time. We could
save our image if we wish but then we would not be able to perform
further analyses upon it (and nor would our colleagues). So what we
can do is save the raw data itself. NumPy again helps us here:

    np.savetxt("data.csv", data, delimiter=",")

If we look at our data file:

    data head.csv

It has no context, nothing. We can add information to our file to
record:

* What the data is.
* What produced it i.e. the provenance of this data.

    import os

    header = "Predator-prey Lotka-Volterra simulation data\n"
    header += "Produced by " + os.path.basename(__file__) + " on " + \
        time.asctime( time.localtime(time.time()))
    header += "\nTime-step, predator population, prey population"
    np.savetxt(output_file, results, delimiter=",", header=header)

Now if we rerun our script and look at our data file it's been stamped
with information about how and when it was produced and what it
is.

We can load this into Python using `np.loadtxt` which will ignore the
lines beginning with `#` which are treated as comments.

## Key points

* Write code for humans not computers
* Sensible variable and function names help make code self-documenting
* Add comments to explain why the code as it is or to explain code
that might otherwise be cryptic
* Record meta-data and provenance information in data files
