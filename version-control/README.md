Basic use
=========

Learning objectives
-------------------

* Draw a diagram showing the places version control stores
  information.
* Check out a working copy of a repository.
* View the history of changes to a project.
* Explain why working copies of different projects should not overlap.
* Add files to a project.
* Commit changes made to a working copy to a repository.
* Update a working copy to get changes from the repository.
* Compare the current state of a working copy to the last update from
  the repository, and to the current state of the repository.
* Explain what "version 123 of `xyz.txt`" actually means.

Key points
----------

* Version control is a better way to manage shared files than email or
  shared folders.
* The master copy is stored in a repository.
* Nobody ever edits the master directory: instead, each person edits a
  local working copy.
* People share changes by committing them to the master or updating
  their local copy from the master.
* The version control system prevents people from overwriting each
  other's work by forcing them to merge concurrent changes before
  committing.
* It also keeps a complete history of changes made to the master so
  that old versions can be recovered reliably.
* Version control systems work best with text files, but can also
  handle binary files such as images and Word documents.
* Every repository is identified by a URL.
* Working copies of different repositories may not overlap.
* Each changed to the master copy is identified by a unique revision
  number.
* Revisions identify snapshots of the entire repository, not changes
  to individual files.
* Each change should be commented to make the history more readable.
* Commits are transactions: either all changes are successfully
  committed, or none are.
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

* Explain what causes conflicts to occur and how to tell when one has
  occurred.
* Resolve a conflict.
* Identify the auxiliary files created when a conflict occurs.

Key points
----------

* Conflicts must be resolved before a commit can be completed.
* Subversion puts markers in text files to show regions of conflict.
* For each conflicted file, Subversion creates auxiliary files
  containing the common parent, the master version, and the local
  version.
* `svn resolve $FILES` tells Subversion that conflicts have been
  resolved.

Recovering old versions
=======================

Learning objectives
-------------------

* Discard changes made to a working copy.
* Recover an old version of a file.
* Explain what branches are and when they are used.

Key points
----------

* Old versions of files can be recovered by merging their old state
  with their current state.
* Recovering an old version of a file does not erase the intervening
  changes.
* Use branches to support parallel independent development.
* `svn revert` undoes local changes to files.
* `svn merge` merges two revisions of a file.

Setting up a repository
=======================

Learning objectives
-------------------

* How to create a repository.

Key points
----------

* `svnadmin create $NAME` creates a new repository.
* Repositories can be hosted locally, on local (departmental) servers,
  on hosting services, or on their owners' own domains.

Provenance
==========

Learning objectives
-------------------

* What data provenance is.
* How to embed version numbers and other information in files managed
  by version control.
* How to record version information about a program in its output.

Key points
----------

* `$Keyword: …$` in a file can be filled in with a property value each
  time the file is committed.
* Put version numbers in programs' output to establish provenance for
  data.
* `svn propset svn:keywords $PROPERTY $FILES` tells Subversion to
  start filling in property values.
