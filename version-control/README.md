Basic use
=========

Learning objectives
-------------------

* Draw a diagram showing the places version control stores
  information.
* Check out a working copy of a repository.
* View the history of changes to a project.
* Add files to a project.
* Commit changes made to the working copy.
* Get changes from an upstream repository.
* Compare the current state of a working copy to the most recent
  update from the upstream repository.
* Explain what "version 123 of `xyz.txt`" actually means.

Key points
----------

* Version control is a better way to manage shared files than email or
  shared folders.
* People share their changes by committing them to public repositories
  and fetch other's changes by updating their local copy from public
  repositories.
* The version control system prevents people from overwriting each
  other's work by making merges explicit.
* It also keeps a complete history of changes made to the master so
  that old versions can be recovered reliably.
* Version control systems work best with text files, but can also
  handle binary files such as images and Word documents.
* Every repository is identified by a URL.
* Each change to the master copy is identified by a unique revision
  ID.
* Revisions identify snapshots of the entire repository, not changes
  to individual files.
* Each change should be commented to make the history more readable.
* Commits are transactions: either all changes are successfully
  committed, or none are.

Merging conflicts
=================

Learning objectives
-------------------

* Explain what causes conflicts to occur and how to tell when one has
  occurred.
* Resolve a conflict.

Key points
----------

* Conflicts must be resolved before a commit can be completed.
* Most version control systems put markers in text files to show
  regions of conflict.

Recovering old versions
=======================

Learning objectives
-------------------

* Discard changes made to a working copy.
* Recover an old version of a file.
* Explain what branches are and when they are used.

Key points
----------

* Recovering an old version of a file may not erase the intervening
  changes.
* Use branches to support parallel independent development.

Setting up a repository
=======================

Learning objectives
-------------------

* How to create a repository.

Key points
----------

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

* Put version numbers in programs' output to establish provenance for
  data.
