In addition to the generic version control objectives and points.

Basic use
=========

Learning objectives
-------------------

* Explain why working copies of different projects should not overlap.

Key points
----------

* The master copy is stored in a repository.
* Nobody ever edits the master directory: instead, each person edits a
  local working copy.
* The basic workflow for version control is update-change-commit.
* `svn add <em>things</em>` tells Subversion to start managing
  particular files or directories.
* `svn checkout $URL` checks out a working copy of a repository.
* `svn commit -m "$MESSAGE" $THINGS` sends changes to the repository.
* `svn diff` compares the current state of a working copy to the state
  after the most recent update.
* `svn diff -r HEAD` compares the current state of a working copy to
  the state of the master copy.
* `svn history` shows the history of a working copy.
* `svn status` shows the status of a working copy.
* `svn update` updates a working copy from the repository.

Merging conflicts
=================

Learning objectives
-------------------

* Identify the auxiliary files created when a conflict occurs.

Key points
----------

* For each conflicted file, Subversion creates auxiliary files
  containing the common parent, the master version, and the local
  version.
* `svn resolve $FILES` tells Subversion that conflicts have been
  resolved.

Recovering old versions
=======================

Key points
----------

* Old versions of files can be recovered by merging their old state
  with their current state.
* Recovering an old version of a file does not erase the intervening
  changes.
* `svn revert` undoes local changes to files.
* `svn merge` merges two revisions of a file.

Setting up a repository
=======================

Key points
----------

* `svnadmin create $NAME` creates a new repository.

Provenance
==========

Key points
----------

* `$Keyword: …$` in a file can be filled in with a property value each
  time the file is committed.
* `svn propset svn:keywords $PROPERTY $FILES` tells Subversion to
  start filling in property values.
