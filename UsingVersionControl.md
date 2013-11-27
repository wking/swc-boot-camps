# Using Version Control Instructor copy

This is a condensed version of the student notes.

## Additional Items to cover
Things to cover:

* Bash basics
 * TAB completion
 * CTR-A (go to the beginning of a line)
 * Up-arrow (to cycle through history)


## Introduction

Move on to the use of git.

**Start with the powerpoint presentation**.

* Motivate use of git:
 * **Good provenance**, recover previous pieces of work
 * **Resilience**, recover work through mishaps
 * **Distributed development** 
 * **Collaborative work**

## Setting up a local repository

### Preliminaries - check we have git

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
1. Google, it has all the answers

### Creating a repository

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
You can list the defaults:
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
    $cp template.html index.html
```

## Setting up a remote repository

# Checking out the GitHub course material

Want to check out the student branch of the course material:

```
    $ git clone -b students https://github.com/mikej888/2013-12-03-edinburgh.git students 
```