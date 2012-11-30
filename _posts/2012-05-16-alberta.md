---
layout: bootcamp
title: University of Alberta: May 16-17, 2012
venue: University of Alberta
dates: May 16-17, 2012
---
**Starting point for homework**

    import sys

    filename = sys.argv[1]

    source = open(filename, 'r')
    longest = -1
    for line in source:
        longest = max(longest, len(line))
    source.close()
    print 'longest line is', longest

    source = open(filename, 'r')
    shortest = 10000000
    for line in source:
        shortest = min(shortest, len(line))
    source.close()
    print 'shortest line is', shortest

**data.txt**

    Date,Species,Count
    2012-05-14,coyote,5
    2012-05-14,deer,14
    2012-05-14,bear,2
    2012-05-15,rabbit,26
    2012-05-15,bear,1
    2012-05-16,magpie,3

**functional.py**

    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    def for_each(func, values):
        assert len(values) > 0, "Must have some data"
        temp = values[0]
        for v in values[1:]:
            temp = func(temp, v)
        return temp

    numbers = [7, 1, 4, -5, 3]

    print "sum is", for_each(add, numbers)
    print "product is", for_each(mul, numbers)
    print "greatest is", for_each(max, numbers)
    print "least is", for_each(min, numbers)
    print "but what about", for_each(max, [])

**Where:** Computing Sciences Centre (CSC) 1-59, University of Alberta, Edmonton, Alberta.

**When:** May 16-17, 2012.
