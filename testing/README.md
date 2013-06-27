# Testing

![image](media/test-in-production.jpg)

# What is testing?

Software testing is a process by which one or more expected behaviors
and results from a piece of software are exercised and confirmed. Well
chosen tests will confirm expected code behavior for the extreme
boundaries of the input domains, output ranges, parametric combinations,
and other behavioral **edge cases**.

# Why test software?

Unless you write flawless, bug-free, perfectly accurate, fully precise,
and predictable code **every time**, you must test your code in order to
trust it enough to answer in the affirmative to at least a few of the
following questions:

-   Does your code work?
-   **Always?**
-   Does it do what you think it does? ([Patriot Missile Failure][patriot])
-   Does it continue to work after changes are made?
-   Does it continue to work after system configurations or libraries
    are upgraded?
-   Does it respond properly for a full range of input parameters?
-   What's the limit on that input parameter?
-   What about **edge or corner cases**?
-   How will it affect your [publications][]?

## Verification

*Verification* is the process of asking, "Have we built the software
correctly?" That is, is the code bug free, precise, accurate, and
repeatable?

## Validation

*Validation* is the process of asking, "Have we built the right
software?" That is, is the code designed in such a way as to produce the
answers we are interested in, data we want, etc.

## Uncertainty Quantification

*Uncertainty quantification* is the process of asking, "Given that our
algorithm may not be deterministic, was our execution within acceptable
error bounds?" This is particularly important for anything which uses
random numbers, eg Monte Carlo methods.


[patriot]: http://www.ima.umn.edu/~arnold/disasters/patriot.html
[publications]: http://www.nature.com/news/2010/101013/full/467775a.html
