{% extends "_bootcamp.html" %} {% block file_metadata %}  {% endblock
file_metadata %} {% block content %}

Please download:

**Count lines in files or in standard input**
    
    import sys
    
    def counter(source):
        count = 0
        for line in source:
            count += 1
        return count
    
    filenames = sys.argv[1:]
    if len(filenames) == 0:
        print 'STDIN', counter(sys.stdin)
    else:
        for filename in filenames:
            reader = open(filename, 'r')
            count = counter(reader)
            print filename, count

**Count marlins in each file in turn**
    
    # Count marlins in each data file.
    for filename in $*
    do
       grep marlin $filename |\
       wc -l
    done

**Count by date**
    
    echo '# count-by-date.sh' $*
    grep -h -v '#' $* | \
    grep -v Species | \
    cut -d ',' -f 1 | \
    sort | \
    uniq -c

**Count marlins using Python**
    
    my_file = file('fish.txt', 'r')
    sum = 0
    for line in my_file:
        if 'marlin' in line:
            date, species, count = line.split(',')
            sum += int(count)
    print sum

**When:** April 14 & 15th, 2012. **8:30am to 4:30pm.**

**Where:** Room 314 of the Biology and Natural Resources building at Utah State University, 5305 Old Main Hill, Logan, UT.

**Information:** Since 1998, Software Carpentry has taught scientists and engineers the skills and tools they need to use computing more productively. Thanks to a grant from the Sloan Foundation, we are running a two-day workshop Utah State University, followed by an optional 4-8 weeks of self-paced online learning. The workshop covers the core skills a researcher needs to know in order to be productive in a small team:

  * Using the shell to do more in less time
  * Using version control to manage and share information
  * Basic Python programming
  * How (and how much) to test programs
  * Working with relational databas

The online follow-up goes into these topics in more detail, and also touch on
program design and construction, matrix programming, using spreadsheets in a
disciplined way, data management, and software development lifecycles.

In collaboration with Ethan White's lab in the Department of Biology we will
be offering the workshop at Utah State on the weekend of April 14th and 15th.
The workshop is free, you just need to bring a laptop and commit to spending 2
days learning about how to be a better scientific programmer. Space is limited
and signups are on a first come first serve basis.

For more information, please see [http://software-carpentry.org](http
://software-carpentry.org), or contact us by email at info@software-
carpentry.org. You can also feel free to email Ethan (ethan.white@usu.edu)
with any questions.

{% endblock content %}

