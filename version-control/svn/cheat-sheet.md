Basic use
=========

* Create a local repository from a public repository at `$URL`:

        $ svn checkout $URL

* Start tracking a new file (or directories):

        $ svn add $FILES

* Remove a file (or files) with the next commit:

        $ svn rm $FILES

* Commit local changes to the public repository:

        $ svn commit -m "$MESSAGE" $THINGS

Merging
=======

* Update your working copy from the public repository:

        $ svn update

* Merge new commits from the public repository:

        $ svn merge

* Mark conflicts as resolved:

        $ svn resolve $FILES

Comparing changes
=================

* Compare the current working directory to the last commit:

        $ svn diff

* Compare the current working directory with the state of the master
  copy:

        $ svn diff -r HEAD

Browsing history
================

* Check your local state:

        $ svn status

* View past commits:

        $ svn history

* Who wrote this line, and what were they thinking?

        $ svn blame $FILES

Recovering old versions
=======================

* Undo local changes since the last commit:

        $ svn revert

Setting up a repository
=======================

* Create a new repository in a new $NAME directory:

        $ svnadmin create $NAME

Provenance
==========

* Add a property-value marker to be filled in with each commit:

        $Keyword: …$

* Start filling in property values:

        $ svn propset svn:keywords $PROPERTY $FILES
