Configuring
===========

* Tell Git who you are:

        $ git config --global user.name 'User Name'
        $ git config --global user.email 'user@email.com'

* Customize the user interface:

        $ git config --global core.editor nano
        $ git config --global color.ui auto

Basic use
=========

* Create a local repository from a public repository at `$URL`:

        $ git clone $URL

* Stage a (possibly new) file (or files) for the next commit:

        $ git add $FILES

* Remove a file (or files) with the next commit:

        $ git rm $FILES

* Commit any local changes to the local repository:

        $ git commit -a -m "$MESSAGE"

* Push any local commits to a public repository (e.g. `origin`):

        $ git push origin

Merging
=======

* Update your local view of a public repository (e.g. `origin`):

        $ git fetch origin

* Merge new commits from another branch (e.g. the `origin/master`
  branch tracking the `master` branch of the `origin` repository):

        $ git merge origin/master

* Mark conflicts as resolved:

        $ git add $FILES

* Instead of merging `origin/master` into your local branch, you can
  rebase your local branch onto `origin/master` (useful options:
  `-i`):

        $ git rebase origin/master

Comparing changes
=================

* Compare the current working directory to the staging area:

        $ git diff

* Compare the staging area to the last commit:

        $ git diff --cached

* Compare the current working directory to the last commit:

        $ git diff HEAD

Browsing history
================

* Check your local state:

        $ git status

* View past commits (useful options: `--oneline`, `--graph`,
  `--decorate`, `--stat`, …):

        $ git log

* Who wrote this line, and what were they thinking?

        $ git blame $FILES
        $ git show $COMMIT

Recovering old versions
=======================

* Undo local changes to `$FILES` since the last commit:

        $ git checkout $FILES

* Checkout `$FILES` as they were during `$COMMIT`:

        $ git checkout $COMMIT -- $FILES

* Create a new commit backing out changes made by an old commit:

        $ git revert $COMMIT

Setting up a repository
=======================

* Create a new repository in the current directory:

        $ git init

Provenance
==========

* Tag releases:

        $ git tag v1.2.3
        $ git push --tags origin

* Incorperate the tags into any releases.  For example, the Git
  project extracts [version information][git-version-gen] when you
  [compile the project][git-makefile].  Most Python projects just
  increment `package.__version__` by hand
  (e.g. [pygit2][pygit2-version]).

Branches
========

* What branch am I on?  What other branches are there?

        $ git branch

* Make a new branch (e.g. `some-feature`):

        $ git branch some-feature

* Change the current branch (e.g. to `some-feature`) and update the
  staging area and working directory:

        $ git checkout some-feature

Remotes
=======

* List configured remotes (URL nicknames):

        $ git remote

* List configured remotes with push/pull URLs:

        $ git remote -v

* Add a new remote:

        $ git remote add $NAME $URL

Manipulating history
====================

* Squash new changes onto the most recent commit:

        $ git commit --amend …

* Move the current branch to `$COMMIT` without touching the staging
  area or working directory:

        $ git reset $COMMIT

* Move the current branch to `$COMMIT` while also resetting the
  staging area and working directory:

        $ git reset --hard $COMMIT


[git-version-gen]: http://git.kernel.org/cgit/git/git.git/tree/GIT-VERSION-GEN
[git-makefile]: http://git.kernel.org/cgit/git/git.git/tree/Makefile
[pygit2-version]: https://github.com/libgit2/pygit2/blob/master/pygit2/version.py
