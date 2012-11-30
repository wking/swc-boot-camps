---
layout: bootcamp
title: 'Michigan State University: May 07-08, 2012'
venue: Michigan State University
dates: May 07-08, 2012
---
**Database file**: [experiments.db](http://software-carpentry.org/experiments.db)

![](http://software-carpentry.org/3_0/db/database-tables.png)

**Querying a Database with Python**

    import sqlite3
    connection = sqlite3.connect("experiments.db")
    cursor = connection.cursor()
    cursor.execute("SELECT FirstName, LastName FROM Person;")
    results = cursor.fetchall();
    for r in results:
        print r[0], r[1]
    cursor.close();
    connection.close();

**Starting point for Monday night exercise**

    import sys

    def count_birds(reader):
        reader.readline() # first line is header, so ignore
        total = 0
        for line in reader:
            date, breed, count = line.split(',')
            count = int(count)
            total += count
        return total

    grand_total = 0
    for filename in sys.argv[1:]:
        source = open(filename, 'r')
        total = count_birds(source)
        grand_total += total
        print total, filename
        source.close()
    print grand_total, 'total'

**When:** May 7-9, 2012.

**Where:**Michigan State University.
