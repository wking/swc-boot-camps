# Using Version Control Instructor copy

This is a condensed version of the student notes. Items covered:

 - [Additional items to cover](#additional)
 - [Introduction](#intro)
 - [Setting up a local repository](#localrep)
    - [Check we have git](#check)
    - [Creating a repository](#creating)
    - [Other things one can do](#other)
    - [Tagging](#tagging)
    - [Branching](#branching)
 - [Setting up a remote repository](#remoterep)
 - [Checking out the Student GitHub material](#student)

<a name="additional"></a>
# Additional Items to cover
Things to cover:

* Bash basics
 * TAB completion
 * CTR-A (go to the beginning of a line)
 * Up-arrow (to cycle through history)

<a name="intro"></a>
# Introduction

Move on to the use of git.

**Start with the powerpoint presentation**.

* Motivate use of git:
 * **Good provenance**, recover previous pieces of work
 * **Resilience**, recover work through mishaps
 * **Distributed development** 
 * **Collaborative work**

<a name="localrep"></a>
# Setting up a local repository

<a name="check"></a>
## Preliminaries - check we have git

1. Check that we have ```git```
```
    $ git --version
    git version 1.7.9
```

1. Getting help
```
    git help
```
```
    git help --all
```
```
    git help checkout
```

1. Any other problems Google it, Google has all the answers

<a name="creating"></a>
## Creating a repository

Scenario - you wish to create a web site. You want to work on it from various machines and may invite colleagues to work on it too.

1. Create the working directory
```
    $ mkdir html
    $ cd html
```

1. Initialize the repository:
```
    $ git init
    Initialized empty Git repository in /home/mario/html/.git/
```

1. This is now our *working directory*, quick inspection:
```
    ls -A
    .git
```
`.git` directory contains Git's configuration files. Be careful not to accidentally delete this directory! 
1. Tell git who we are:
```
    $ git config --global user.name "Your Name"
    $ git config --global user.email "yourname@yourplace.org"
```
also useful to specify what your default editor is going to be:
```
    $ git config --global core.editor "vi"
```
You can list the defaults already defined:
```
    $ git config -l
```
Global information is stored in a ```.gitconfig``` file so you can do:
```
    $ cat ~/.gitconfig
```
1. Create a ```template.html``` file:
```
    <!DOCTYPE html>
    <html>
    <head>
    <title></title>
    </head>
    <body>
    <h1>

    </h1>

    </body>
    </html>
```

1. Find out what the ```git status``` is:
```
    $ git status
     # On branch master
     #
     # Initial commit
     #
     # Untracked files:
     #   (use "git add <file>..." to include in what will be committed)
     #
     #       template.html
    nothing added to commit but untracked files present (use "git add" to track)
```
which basically tells you what to do.

1. Add the file:
```
   $ git add template.html
```
Try running ```git status``` after each of the steps to show the differences.

1. Now commit the file:
```
    $ git commit template.html
```
1. Add another file:
```
    $ cp template.html index.html
```
1. Edit the page to vaguely make it look like a home page. Add a title, a heading and a little bit of content.
```
    <!DOCTYPE html>
    <html>
    <head>
    <title>My Home Page</title>
    </head>
    <body>
    <h1>Welcome to my Home Page</h1>
    <p>
    I would like to welcome you to my home page.
    </p>

    </body>
    </html>
```

1. Add and commit the file:
```
    $ git add index.html
    $ git commit -m"index.html: added a landing page." index.html
    [master 8353923] index.html: added a landing page.
    1 files changed, 13 insertions(+), 0 deletions(-)
    create mode 100644 index.html
```
Run ``git status``

1. Checking your history of changes:
```
    $ git log
```
More useful versions of the command:
```
    $ git log --relative-date
```
or
```
    $ git log --oneline --graph
```

1. Add an image to the web page:
```
    $ mkdir images
    $ cd images
    $ wget http://www2.epcc.ed.ac.uk/~mario/man.png # or
    $ wget http://www2.epcc.ed.ac.uk/~mario/woman.png
    $ cd ..
    $ git add images
```

1. Edit the ```index.html``` file with the lines:
```
    <p>
    <img src="images/man.png"/>
     This is me.
    </p>
```
Add the file to git:
```
    git add index.html
```
and commit
```
    $ git commit -m"Added an image of myself."
```
or can short circuit by using:
```
    $ git commit -m"Added an image of myself." index.html
```
and avoid the ```git add``` step.

<a name="other"></a>
## Other things one can do

Can demonstrate these or talk about them:

Adding all files in the current directory recursively:
```
    $ git add .
```

Committing all current *working files*:
```
    $ git commit -a
```

Show the difference between a working file and a committed file:
```
    $ git diff filename
```
or with a particular previous commit:
```
    $ git diff COMMITID
```
where `COMMITID` is the hash for a particular commit (can use the 6 digit form).

Recovering last checked-out version and clobbering existing changes:
```
    $ git commit index.html
```
or can go to an earlier state
```
    $ git checkout COMITD
```
creates a detached `HEAD` though but one can have a look and then go back to the original code:
```
     $ git checkout master
```
<a name="tagging"></a>
## Tagging

Can tag to have more memorable identifiers:

```
    $ git tag v1.0
```
can view the tags:
```
    $ git tag
    v1.0
```

<a name="branching"></a>
## Branching

** Do the second half of the presentation to motivate this section**.

1. Find out what branch we are on:
```
    $ git branch
    * master
```
1. Suppose we want to test a new feature, like cascading style sheets without impacting on our main development. Can create a new branch to do this:
```
    $ git banch css_test
```
Now if we do:
```
    $ git branch
      css_test
    * master
```
1. Now switch to the new branch:
```
    $ git checkout css_test
    Switched to branch 'css_test'
```
1. Create a stylesheet `mystyle.css`
```
     /* make all paragraph text bold and red */
     p
     {
        color: red;
        font-weight: bold;
     }
```

1. Associate with your `index.html` file by adding the line:
```
    <head>
      <title>My Home Page</title>
      <link rel="stylesheet" type="text/css" href="mystyle.css"/>
    </head>
```
Test to see. Suppose that for some bizarre reason you are happy with this. You add the files and commit:
```
    $ git add .
    $ git commit -m"Cool red text added."
```

1. Go back to the master thread:
```
    $ git checkout master
```
Note that all the new content has gone (it's still in the `css_test` branch). If you are really happy you can import the content from `css_test` by doing:
```
    $ git merge css_test
    Updating ebb2075..e003ffe
    Fast-forward
     index.html  |    1 +
     mystyle.css |    6 ++++++
     2 files changed, 7 insertions(+), 0 deletions(-)
     create mode 100644 mystyle.css
```
Check by viewing the page on your browser. Also, see the output to:
```
    $ git --oneline --graph
```

<a name="remoterep"></a>
# Setting up a remote repository

<a name="student"></a>
# Checking out the Student GitHub material

Want to check out the student branch of the course material:

```
    $ git clone -b students https://github.com/mikej888/2013-12-03-edinburgh.git students 
```