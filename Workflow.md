Repository structure
====================

There is a [central repository][boot-camps] for all boot camp
material.  The `master` branch has the current state-of-the-art source
for the instructors' projected content, handouts, boot camp homepage,
….  If we can't agree on a canonical representation, there may be a
handful of feature branches with alternative content.

NOTE: SWC has not yet formed a consensus about the structure of the
`master` branch.

Topics will live in per-subject subdirectories, ideally organized in
half-day-sized chunks.

    .
    ├── README.md
    ├── debugging
    │   ├── README.md
    │   …
    ├── make
    │   ├── README.md
    │   ├── example-project
    │   …
    ├── python
    │   ├── README.md
    │   ├── animals.txt
    │   …
    ├── shell
    │   …
    ├── version-control
    │   ├── git
    │   │   ├── basic
    │   │   │   …
    │   │   └── advanced
    …   …       …
  
    Figure 1: Example directory tree for the current master tip.
    Sections should be in half-day-ish chunks.  Complicated topics
    that need more detailed coverage (e.g. version control) can have
    nested sub-sections.

Cloning the master repository
=============================

If you haven't worked on any boot camp content before, you'll need to
clone the master repository.  You'll also want a way to publish your
changes.  Because [GitHub pull requests][gh-pull] require the pulled
head to be on GitHub, that means you'll need a [GitHub
account][gh-account].  Log into GitHub, and [fork][gh-fork] the
[boot-camps repository][boot-camps].  Clone your fork with:

    $ git clone https://github.com/your-username/boot-camps.git
    $ cd boot-camps

You'll want to track the SWC repository to stay abreast of changes, so
add it as a remote:

    $ git remote add swc https://github.com/swcarpentry/boot-camps.git

Now you're ready to start hacking away.

Creating a new boot camp
========================

An instructor preparing for a new boot camp should create a per-camp
branch from the upstream `master`:

    $ git checkout -b 2012-12-my-camp swc/master

and optionally merge feature branches they like:

    $ git merge swc/git-wtk

This gives a starting point for developing your boot camp.

    -o--o--o--o--o    swc/master    (same as local master)
      \-o--o      \   swc/git-wtk
            \------o  2012-12-my-camp
  
    Figure 2: Graph of commits for the beginning of the
    2012-12-my-camp branch.  Time increases to the right.  Commits
    are marked with “o”.  ASCII art connects child commits with their
    parents.  The merge of a well-maintained feature branch should be
    painless.

Developing boot camp content
============================

Camp-specific content
---------------------

If you don't have strong ideas about the content, there's probably not
much to do here besides tweaking a few boot-camp-specific bits
(location, dates, master-index, …).  These changes should go into the
boot camp branch:

    $ emacs README.md
    (edit linking)
    $ git commit -am 'README.md: link to shell, git/basic, and git/advanced'
    $ emacs README.md
    (localize for your boot camp)
    $ git commit -am 'README.md: localize for 2012-12 boot camp at my house'

This creates:

    -o--o--o--o--o          swc/master
      \-o--o      \         swc/git-wtk
            \------o--a--b  2012-12-my-camp
  
    Figure 2: Boot-camp-specific changes go into the boot-camp-specific
    branch.  Example log:
  
      commit  message
      ------  -----------------------------------------------------
      a       README.md: link to shell, git/basic, and git/advanced
      b       README.md: localize for 2012-12 boot camp at my house

General content
---------------

If you want to change some of the general content, you should make
your change on the master branch (or the feature branch like
“git-wtk”).

    $ git checkout -b typo-fix swc/master
    $ sed -i 's|origin\\master|origin/master|g' version-control/git/basic/README.md
    $ git commit -am 'git/basic: fix origin\master -> origin/master typo'

Publish your feature branch in your GitHub repository:

    $ git push origin typo-fix

And make a pull request on GitHub to get your feature branch merged
upstream.

While the feature branch is being discussed upstream, go ahead and
merge your changes into your boot camp branch.

    $ git checkout 2012-12-my-camp
    $ git merge typo-fix

This creates:

                  /-a----\---\   typo-fix
    -o--o--o--o--o--------\---c  swc/master
      \-o--o      \        \     swc/git-wtk
            \------o--o--o--b    2012-12-my-camp
  
    Figure 3: You can't push to master, so you made a new “typo-fix”
    branch.  Later on, a SWC dev will merge it into master.  Example
    log:
  
    commit  message
    ------  --------------------------------------------------
    a       git/basic: fix origin\master -> origin/master typo
    b       merge recent master branch updates
    c       git/basic: merge origin\master typo fix

After your feature branch has been merged into your boot camp branch
and the upstream branch, it no longer needs a convenient name.  Delete
the branch itself:

    $ git branch -d typo-fix

You'll also want to remove the branch from your public GitHub
repository:

    $ git push origin :typo-fix

Publishing boot camp websites
=============================

NOTE: SWC has not yet formed a consensus about organizing boot camp
websites.  Until it has, take this section with a grain of salt.

The boot camp source should be set up for easy compilation into a
web-site.  Once you build the website, you can publish it wherever you
like (e.g. on a departmental server).  If you want to publish your
boot camp website on the [SWC GitHub page][camps] at

    http://swcarpentry.github.com/boot-camps/2012-12-my-camp

you'll need to edit the `gh-pages` branch.  The [pages][gh-pages] are
built with [Jekyll][], so consult the Jekyll docs for details on
markup, templates, ….

Keeping the master gh-pages branch up-to-date amongst several
simultaneous boot camps may involve some [submodule
shenanigans][website-readme].

Post-boot-camp archival
=======================

The boot camp branch is a clean record of how your source developed
and the particular material that you presented to your students.  You
should publish your final branch state on your GitHub repository:

    $ git push origin 2012-12-my-camp

and submit a pull request (the base branch should match your
`YYYY-MM-LOCATION` branch tag).  After the pull request is accepted
(which shouldn't take long, since there shouldn't be any controversy
over its content), the developer who merged the pull request will tag
the boot camp branch and delete the branch itself

    $ git tag 2012-12-my-camp swc/2012-12-my-camp
    $ git push swc tag 2012-12-my-camp
    $ git push swc :heads/2012-12-my-camp

Git branches are basically tags that move.  Once the boot camp is done,
there's no need for its tip commit to change, so you might as well
mark it with a tag.  After your branch has been tagged upstream, you
can fetch the new tag with:

    $ git fetch swc

The new tag should match your branch tip, so you can safely delete the
branch:

    $ git branch -d 2012-12-my-camp

Then push any new tags to your public GitHub repository and remove the
old branch.

    $ git push --tags origin
    $ git push origin :heads/2012-12-my-camp

Tweaks
======

The following notes provide helpful hints for managing your
repositories.  Feel free to skip them if they don't sound interesting.

Simplifying your local repository
---------------------------------

If you don't like remote branches cluttering your local repo, you can
clone a single branch of the master repository using:

    $ git clone --single-branch https://github.com/your-username/boot-camps.git

You can also limit the branches you fetch from upstream.  After adding
the `swc` remote, run:

    $ git config remote.swc.fetch +refs/heads/master:refs/remotes/swc/master

After this, future calls to `git fetch` will retrieve only the
`master` branch from `swc` and its associated tags, ignoring other
branches and unrelated tags.

Disjoint branches
-----------------

If you really want to roll your own content, feel free to skip the
master branch entirely.

    -o--o--o--o--o        swc/master
      \-o--o              swc/git-wtk
              I--o--o--a  2012-12-my-camp
  
    Figure 4: A disjoint branch (2012-12-my-camp).  The commit “I”
    has no parents.  Different branches stored in the same repository
    don't need to share any common commits.  They're still addressing
    the same goal, and having them in the same repo means its easier to
    clone/fetch/diff/….


[boot-camps]: https://github.com/swcarpentry/boot-camps
[gh-pull]: https://help.github.com/articles/using-pull-requests
[gh-account]: https://github.com/signup/free
[gh-fork]: https://help.github.com/articles/fork-a-repo
[camps]: http://swcarpentry.github.com/boot-camps/
[gh-pages]: https://help.github.com/categories/20/articles
[Jekyll]: https://github.com/mojombo/jekyll
[website-readme]: https://github.com/swcarpentry/boot-camps/blob/gh-pages/README
