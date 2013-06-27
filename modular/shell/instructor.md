# Introduction to the shell

* Name-drop [terminal][] as distinct from [shell][].
    * Get folks to a terminal.
* Mention [Bash][] as a common default shell
    * If you're in a different shell, run `bash` to get Bash.
    * Mention commonality between shells, but existence of differences.
        * Maybe mention [POSIX][].
    * [Name-drop the Advanced Bash-Scripting Guide][ABSG].
* Have them clone the boot camp repository:

        $ git clone -b YYYY-MM-PLACE --single-branch git://github.com/swcarpentry/boot-camps.git

* `echo` (e.g. `echo Hello, World`)
    * Remind them to press enter.
    * Useful for printing from a shell script, for displaying
      variables, and for generating known values to pass to other
      programs.

# File systems

* `pwd` (print working directory)
* `ls` (list directory contents)
* Directory/folder equivalence
* Directories are just lists of files or other directories.
* New-terminals/shells start in the *home* directory.
    * Every user has their own home directory.
* `whoami` (what is my user name)

# File types

* `ls` output is colored (run it in the home directory).
    * Directories are usually blue (customize with `~/.dir_colors`).
* `touch` (create an empty file)

        $ touch testfile

* `ls` again, see `testfile`.  Note that it's white (a general file).
* `ls -F`, because some terminals don't support colors.
    * Directories marked with a trailing slash (/)
    * Executables marked with a trailing star (*)
* `ls -l` to get permissions, ownership, size, modification times, etc.
    * If the entry is a directory, then the first letter will be a `d`.
    * The fifth column shows you the size of the entries in bytes.
        * Notice that `testfile` has a size of zero.
* `rm` to remove files and (with `-r`) directories.

        $ rm testfile

* Run `ls` again, and see that `testfile` is gone.

# Changing Directories

* `cd` (change directory) into the directory they'd previously cloned

        $ cd boot-camps

* `ls` to see what's in the newly current directory
* `cd` into the exercises section, then `ls` again, and `ls -F`.
    * You may want to `cd "$LOC1"; cd "$LOC2"` instead of jumping
      directly via `cd "$LOC1/$LOC2"`.
* `cd` without arguments takes you back to your home directory
* Change back into the examples directory

# Arguments

* `-F` and `-l` are arguments to `ls`
* `ls` takes lots of arguments
* `man` pages (when they exist) usually describe these options

        $ man ls

    * `man` displays the page using your `PAGER`.  This is probably
      `less`.

        * Page down with space or the "page down" key
        * Page up with `b` or the "page up" key
        * Search by regexp with `/`
        * Get help with `h` with other `less` key bindings
        * Quit with `q`

* `man find` for a complicated page
    * Don't worry about learning all of this, just refer back to it as
      needed.

## Exercise: `ls` options

1. Use the manual page for `ls` to guess what you would expect from
   using the arguments `-l`, '-t', '-r' at the same time.
2. Try the following and see if you can figure out what they do,
   either by examining the results or consulting the manual page.
    * `ls -lS` (equivalent to `ls -l -S`)
    * `ls -lt` (equivalent to `ls -l -t`)
    * `ls -1`  (that's the number one, not a letter 'ell')

# Examining the contents of other directories

* Instead of `cd "$LOC"; ls`, you can use `ls "$LOC"`
    * Look at a few directories in this repository
* Use `cd "$LOC"` to change into a few directories as well
    * Folks should be comfortable with `cd "$LOC1/$LOC2"` by now

# Full vs. relative paths

* Directories are arranged in a single hierarchy, based on the
  *root directory* `/`.
* Full (aka absolute) paths include everything from the root down.
* Relative paths don't start with the root directory, and are
  (usually) interpreted relative to the current working directory
  (`pwd`).
* Examples with full paths:

        $ cd /home/swc/boot-camps/modular

* Examples with relative paths:

        $ cd
        $ cd boot-camps/modular

# Exercise: Listing `/bin`

List the contents of the `/bin` directory (a full path).  Do you see
anything familiar in there?

# Saving time with shortcuts, wild cards, and tab completion

## Path shortcuts

* `~` for your home directory
* `..` for the parent of the current working directory
* Chainable.  For example: `ls ../../` or `ls ~/../`.
* `.` for the current directory
    * Equivalent commands:
        * `ls`
        * `ls .`
        * `ls ././././.`
* These shortcuts are not necessary, they are provided for your
  convenience.

# Example: Cochlear implants

Introduce the [cochlear implant example][cochlear] to practice with
the coming topics.

## Wildcards

* Docs for wildcards are in in glob(7).
* For cochlear implants, cd into `data/THOMAS` for this.
* `ls`, there are a bunch of files with four-digit names
* `ls *`, same list
* `ls *1', all files ending with 1
* `ls /usr/bin/*.sh`, an absolute path example
* `ls *4*1`, compound wildcards
    * These are expanded *by the shell*, before being passed to the
      command, so the following are identical;

            $ ls *4*1
            $ ls 0241 0341 0431 0481

### Exercise: Globbing with `ls`

Do each of the following using a single `ls` command without
navigating to a different directory.

1.  List all of the files in `/bin` that contain the letter `a`
2.  List all of the files in `/bin` that contain the letter `a` or the letter `b`
3.  List all of the files in `/bin` that contain the letter `a` AND the letter `b`

## Tab completion

* Change to the home directory.
* Work back to the coclear implant example data using tab completion

        $ cd b<tab>
        $ cd boot-camps/
        $ cd boot-camps/<tab><tab>
        …list of choices…

* Tab completion for executables in the `PATH`.

        $ e<tab><tab>
        $ ec<tab>
        $ echo

## Command History

* Work through history with up and down arrows.
* `^C` to cancel the command you are writing and give you a fresh
  prompt.
* `^R` to reverse-search through your command history.
* `history` to print your history
    * `history | grep …` to grab some useful command
    * `!123` to reuse the 123rd command in your history

### Excercise: History

1. Find the line number in your history for the last exercise (listing
   files in `/bin`) and reissue that command.

## Which program?

* `ls`, `rm`, `find`, … are stand-alone programs.
* `command`, `shift`, `cd`, `echo`, `pwd`, … are likely shell builtins
* `which COMMAND` to look up the command in your `PATH`
* `command -V COMMAND` to get useful info:

        $ command -V cd
        cd is a shell builtin
        $ command -v find
        /usr/bin/find
        $ command -V ls
        ls is aliased to `ls --color=auto'
* Explain `PATH` lookup (`echo $PATH`)
* In the example directory, there's a `hello` script
    * Try to run it with `hello`.  Oops, not in the `PATH`!
    * Give a path with `./hello`.  Success!
        * Something that `.` is useful for!
    * `/home/…/boot-camps/…/hello`
    * `../exercises/hello`
    * Only get `PATH` lookups when there aren't any `/` in your command.

## Examining Files

We now know how to switch directories, run programs, and look at the
contents of directories, but how do we look at the contents of files?

* `cat` (concatenate).  In the cochlear implant example,

        $ cat ex_data.txt
        $ cat ex_data.txt ex_data.txt

### Exercise: 

1.  Print out the contents of the `dictionary/dictionary.txt` file.
    What does this file contain?

2.  Without changing directories, use one short command to print the
    contents of all of the files in the
    `/home/…/boot-camps/…/exercises/hearing/data/THOMAS` directory.

## Paging

* How to view large files?
* `less` (is `more`)

        $ less ~/boot-camps/…/exercises/dictionary/dictionary.txt

* `less` opens the file and lets you navigate through it.
* As mentioned with the `man` page stuff earlier, `h` for help, `q` to
  quit.
* Searches with `/` don't wrap, search from the beginning of the file.

### Example: paging through man pages

Use the commands we've learned so far to figure out how to search
in reverse while using `less`.

## Redirection

* Back to the hearing example!
* Enter the `Bert` subdirectory.
* Print all the experimental results

        $ cat au*

* Redirect that into a file:

        $ cat au* > ../all_data

* Examine `all_data` with `less`.
* If `all_data` had already existed, we would overwritten it.
* `>` tells the shell to take the output from what ever is (stdout) on
  the left and dump it into the file on the right.
* `>>` is the same, but it appends instead of overwriting.

### Exercise: Redirection

Use `>>`, to append the contents of all of the files whose names
contain the number 4 in the `gerdal` directory to the existing
`all_data` file. Thus, when you are done `all_data` should contain all
of the experiment data from `Bert` and any experimental data file from
`gerdal` with filenames that contain the number 4.

## Creating, moving, copying, and removing

We've created a file called `all_data` using the redirection operator
`>`. This file is critical—it's our analysis results—so we want to
make copies so that the data is backed up.

* `cp` (copy)

        $ cp all_data all_data_backup

* `mv` (move)

        $ mv all_data_backup /tmp/

    * Explain what `/tmp` is for, and that it doesn't (usually)
      survive reboots.
* Rename with `mv`.

        $ mv all_data all_data_IMPORTANT

* `rm` (remove)

        $ rm /tmp/all_data_backup

* `mkdir` (make directory)
* By default, `rm`, will NOT delete directories.  Use `-r` (carefully!)
    * Also, `rmdir` (remove directory)

### Excercise: Rename, create, and copy

1.  Rename the `all_data_IMPORTANT` file to `all_data`.
2.  Create a directory in the `data` directory called `foo`
3.  Then, copy the `all_data` file into `foo`

## Count the words

* `wc` (word count).  From `hearing/data`:

        $ wc Bert/* gerdal/*4*

* Three columns for each file:
    * Number of lines
    * Number of words
    * Number of characters
* The final line contains this information summed over all of the
  files.
* Check summation:

        $ wc all_data

* Compare byte size with character count

        $ ls -l all_data

### Exercise: Longest line length

Figure out how to get `wc` to print the length of the longest line in
`all_data`.

## The awesome power of the Pipe

Suppose I wanted to only see the total number of character, words, and
lines across the files `Bert/*` and `gerdal/*4*`. I don't want to
see the individual counts, just the total. Of course, I could just do:

    wc all_data

Since this file is a concatenation of the smaller files. Sure, this
works, but I had to create the `all_data` file to do this. Thus, I
have wasted a precious 10445 bytes of hard disk space. We can do this
*without* creating a temporary file, but first I have to show you two
more commands: `head` and `tail`. These commands print the first few,
or last few, lines of a file, respectively. Try them out on
`all_data`:

    head all_data
    tail all_data

The `-n` option to either of these commands can be used to print the
first or last `n` lines of a file. To print the first/last line of the
file use:

    head -n 1 all_data
    tail -n 1 all_data

Let's turn back to the problem of printing only the total number of
lines in a set of files without creating any temporary files. To do
this, we want to tell the shell to take the output of the `wc Bert/*
gerdal/*4*` and send it into the `tail -n 1` command. The `|`
character (called pipe) is used for this purpose. Enter the following
command:

    wc Bert/* gerdal/Data0559 | tail -n 1

This will print only the total number of lines, characters, and words
across all of these files. What is happening here? Well, `tail`, like
many command line programs will read from the *standard input* when it
is not given any files to operate on. In this case, it will just sit
there waiting for input. That input can come from the user's keyboard
*or from another program*. Try this:

    tail -n 2

Notice that your cursor just sits there blinking. Tail is waiting for
data to come in. Now type:

    French
    fries
    are
    good

then CONTROL+d. You should is the lines:

    are
    good

printed back at you. The CONTROL+d keyboard shortcut inserts an
*end-of-file* character. It is sort of the standard way of telling the
program "I'm done entering data". The `|` character is replaces the
data from the keyboard with data from another command. You can string
all sorts of commands together using the pipe.

The philosophy behind these command line programs is that none of them
really do anything all that impressive. BUT when you start chaining
them together, you can do some really powerful things really
efficiently. If you want to be proficient at using the shell, you must
learn to become proficient with the pipe and redirection operators:
`|`, `>`, `>>`.


### A sorting example

Let's create a file with some words to sort for the next example. We
want to create a file which contains the following names:

    Bob
    Alice
    Diane
    Charles

To do this, we need a program which allows us to create text
files. There are many such programs, the easiest one which is
installed on almost all systems is called `nano`. Navigate to `/tmp`
and enter the following command:

    nano toBeSorted

Now enter the four names as shown above. When you are done, press
CONTROL+O to write out the file. Press enter to use the file name
`toBeSorted`. Then press CONTROL+x to exit `nano`.

When you are back to the command line, enter the command:

    sort toBeSorted

Notice that the names are now printed in alphabetical order.

* * * *
**Short Exercise**

Use the `echo` command and the append operator, `>>`, to append your
name to the file, then sort it and make a new file called Sorted.

* * * *

Let's navigate back to `~/boot-camps/shell/data`. Enter the following command:

    wc Bert/* | sort -k 3 -n

We are already familiar with what the first of these two commands
does: it creates a list containing the number of characters, words,
and lines in each file in the `Bert` directory. This list is then
piped into the `sort` command, so that it can be sorted. Notice there
are two options given to sort:

1.  `-k 3`: Sort based on the third column
2.  `-n`: Sort in numerical order as opposed to alphabetical order

Notice that the files are sorted by the number of characters.

* * * *
**Short Exercise**

1. Use the `man` command to find out how to sort the output from `wc` in
reverse order.

2. Combine the `wc`, `sort`, `head` and `tail` commands so that only the
`wc` information for the largest file is listed

Hint: To print the smallest file, use:

    wc Bert/* | sort -k 3 -n | head -n 1

* * * *

Printing the smallest file seems pretty useful. We don't want to type
out that long command often. Let's create a simple script, a simple
program, to run this command. The program will look at all of the
files in the current directory and print the information about the
smallest one. Let's call the script `smallest`. We'll use `nano` to
create this file. Navigate to the `data` directory, then:

    nano smallest

Then enter the following text:

    #!/bin/bash
    wc * | sort -k 3 -n | head -n 1

Now, `cd` into the `Bert` directory and enter the command
`../smallest`. Notice that it says permission denied. This happens
because we haven't told the shell that this is an executable
file. If you do `ls -l ../smallest`, it will show you the permissions on
the left of the listing.

Enter the following commands:

    chmod a+x ../smallest
    ../smallest

The `chmod` command is used to modify the permissions of a file. This
particular command modifies the file `../smallest` by giving all users
(notice the `a`) permission to execute (notice the `x`) the file. If
you enter:

    ls -l ../smallest

You will see that the file name is green and the permissions have changed.
Congratulations, you just created your first shell script!

# Searching files

You can search the contents of a file using the command `grep`. The
`grep` program is very powerful and useful especially when combined
with other commands by using the pipe. Navigate to the `Bert`
directory. Every data file in this directory has a line which says
"Range". The range represents the smallest frequency range that can be
discriminated. Lets list all of the ranges from the tests that Bert
conducted:

    grep Range *

* * * *
**Short Exercise**

Create an executable script called `smallestrange` in the `data`
directory, that is similar to the `smallest` script, but prints the
file containing the file with the smallest Range. Use the commands
`grep`, `sort`, and `tail` to do this.

* * * *


# Finding files

The `find` program can be used to find files based on arbitrary
criteria. Navigate to the `data` directory and enter the following
command:

    find . -print

This prints the name of every file or directory, recursively, starting
from the current directory. Let's exclude all of the directories:

    find . -type f -print

This tells `find` to locate only files. Now try these commands:

    find . -type f -name "*1*"
    find . -type f -name "*1*" -or -name "*2*" -print
    find . -type f -name "*1*" -and -name "*2*" -print

The `find` command can acquire a list of files and perform some
operation on each file. Try this command out:

    find . -type f -exec grep Volume {} \;

This command finds every file starting from `.`. Then it searches each
file for a line which contains the word "Volume". The `{}` refers to
the name of each file. The trailing `\;` is used to terminate the
command.  This command is slow, because it is calling a new instance
of `grep` for each item the `find` returns.

A faster way to do this is to use the `xargs` command:

    find . -type f -print | xargs grep Volume

`find` generates a list of all the files we are interested in,
then we pipe them to `xargs`.  `xargs` takes the items given to it
and passes them as arguments to `grep`.  `xargs` generally only creates
a single instance of `grep` (or whatever program it is running).

* * * *
**Short Exercise**

Navigate to the `data` directory. Use one `find` command to perform each
of the operations listed below (except number 2, which does not
require a `find` command):

1.  Find any file whose name is "NOTES" within `data` and delete it

2.  Create a new directory called `cleaneddata`

3.  Move all of the files within `data` to the `cleaneddata` directory

4.  Rename all of the files to ensure that they end in `.txt` (note:
    it is ok for the file name to end in `.txt.txt`

Hint: If you make a mistake and need to start over just do the
following:

1.  Navigate to the `shell` directory

2.  Delete the `data` directory

3.  Enter the command: `git checkout -- data` You should see that the
    data directory has reappeared in its original state

**BONUS**

Redo exercise 4, except rename only the files which do not already end
in `.txt`. You will have to use the `man` command to figure out how to
search for files which do not match a certain name.

* * * *



# Bonus material

* Command substitution (`$(command)` and `\`command\``).
* `xargs`
* Aliases (`rm -i`)
* Variables (`PATH`, `PS1`, `PWD`)
* `.bashrc`
* `du` (disk usage)
* `ln` (link)
* `ssh` and `scp` (secure shell and secure copy)
* Regular expressions (with `grep`, `sed`, …)
* Permissions (`ls -l`, `chmod`, `chown`)
* Chaining commands (pipes, file descriptors, fifos, …)


[terminal]: https://en.wikipedia.org/wiki/Terminal_emulator
[shell]: https://en.wikipedia.org/wiki/Unix_shell
[Bash]: http://www.gnu.org/software/bash/
[POSIX]: http://pubs.opengroup.org/onlinepubs/9699919799/idx/shell.html
[ABSG]: http://tldp.org/LDP/abs/html/
[cochlear]: exercises/hearing/
