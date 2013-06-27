**The Problem:** In 2D or 3D, we have two points (p1 and p2) which
define a line segment. Additionally there exists experimental data which
can be anywhere in the domain. Find the data point which is closest to
the line segment.

In the [close_line.py][close-line] file there are four different
implementations which all solve this problem. [You can read more about
them here][evolution-of-a-solution].  However, there are no tests!
Please write from scratch a `test_close_line.py` file which tests the
`closest_data_to_line()` functions.

*Hint:* you can use one implementation function to test another. Below
is some sample data to help you get started.

![image](../../media/evolution-of-a-solution-1.png)

[close-line]: close_line.py
[evolution-of-a-solution]: http://inscight.org/2012/03/31/evolution_of_a_solution/
