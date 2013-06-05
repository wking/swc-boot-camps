# <a id="contents" /> Contents

1. [An overview of the repository structure](#structure)
2. [Cloning the master repository](#clone)
3. [Creating a new boot camp](#new)
4. [Publishing your local work](#push)
5. [Developing boot camp content](#develop)
    1. [Camp-specific content](#camp-specific)
    2. [General content](#general)
6. [Post-boot-camp archival](#archive)
7. [Tweaks and hints](#archive)
    1. [Simplifying your local branch structure](#simple)
    2. [Disjoint branches](#disjoint)
    3. [Avoiding the GitHub website](#hub)

The important parts to get right before your boot camp are
[cloning](#clone), [branch creation](#new), [publishing](#push), and
[development](#develop).  This clone/branch/develop/publish/(merge)
cycle is the common Git workflow, so there are [lots of][git-book]
[tutorials][user-manual] to get you oriented, if the information here
is not sufficient.  Also feel free to ask on the [mailing list][gits]
or [IRC][].

# <a id="structure" /> Repository structure

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

# <a id="clone" /> Cloning the master repository

If you haven't worked on any boot camp content before, you'll need to
clone the master repository.  You'll also want a way to publish your
changes.  Because [GitHub pull requests][gh-pull] require the pulled
head to be on GitHub, that means you'll need a [GitHub
account][gh-account].  Log into GitHub, and [fork][gh-fork] the
[boot-camps repository][boot-camps].  Clone your fork with:

    $ git clone https://github.com/YOU/boot-camps.git
    $ cd boot-camps

You'll want to track the SWC repository to stay abreast of changes, so
add it as a remote and fetch it:

    $ git remote add swc https://github.com/swcarpentry/boot-camps.git
    $ git fetch swc

Now you're ready to start hacking away.

# <a id="new" /> Creating a new boot camp

An instructor preparing for a new boot camp should create a per-camp
branch from the upstream `master`:

    $ git checkout -b 2012-12-my-camp swc/master

and optionally merge feature branches they like:

    $ git merge swc/git-wtk

This gives a starting point for developing your boot camp.

    -o---o---o---o      swc/master    (same as local master)
      \           \
       o---o       \    swc/git-wtk
            \       \
             `-------M  2012-12-my-camp

    Figure 2: Graph of commits for the beginning of the
    2012-12-my-camp branch.  Time increases to the right.  Commits are
    marked with “o”.  ASCII art connects child commits with their
    parents.  The merge of a well-maintained feature branch (marked
    with an “M”) should be painless.

# <a id="push" /> Publishing your local work

The `checkout -b` command mentioned above creates a new branch in your
local repository, but you'll want to publish this branch so others can
see it.  Push your branch to your public repository with:

    $ git push origin 2012-12-my-camp

GitHub doesn't accept pushes via the `git://` protocol, so you'll want
to use an `https://` URL (with optional [password caching][https]) or
[setup SSH keys][ssh] and push over SSH.  You can list remotes and
their associated URLs with `git remote -v` to help you remember what
you've already configured.

You'll want to push again whenever you need to publish additional
local work.

If you have commit access to the [swcarpentry repository][boot-camps],
you can push your branch directly, instead of staging it in *your*
GitHub repository:

    $ git push swc 2012-12-my-camp

# <a id="develop" /> Developing boot camp content

## <a id="camp-specific" /> Camp-specific content

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

    -o---o---o---o              swc/master    (same as local master)
      \           \
       o---o       \            swc/git-wtk
            \       \
             `-------o---A---B  2012-12-my-camp

    Figure 3: Boot-camp-specific changes go into the boot-camp-specific
    branch.  Example log:

      commit  message
      ------  -----------------------------------------------------
      A       README.md: link to shell, git/basic, and git/advanced
      B       README.md: localize for 2012-12 boot camp at my house

## <a id="general" /> General content

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

                   A-------------.    typo-fix
                  /         \     \
    -o---o---o---o-----------\-----C  swc/master
      \           \           \
       o---o       \           \      swc/git-wtk
            \       \           \
             `-------o---o---o---B    2012-12-my-camp

    Figure 4: You can't push to master, so you made a new “typo-fix”
    branch.  Later on, a SWC dev will merge it into master.  Example
    log:

    commit  message
    ------  --------------------------------------------------
    A       git/basic: fix origin\master -> origin/master typo
    B       merge recent master branch updates
    C       git/basic: merge origin\master typo fix

After your feature branch has been merged into your boot camp branch
and the upstream branch, it no longer needs a convenient name.  Delete
the branch itself:

    $ git branch -d typo-fix

You'll also want to remove the branch from your public GitHub
repository:

    $ git push origin :typo-fix

# <a id="archive" /> Post-boot-camp archival

The boot camp branch is a clean record of how your source developed
and the particular material that you presented to your students.  You
should publish your final branch state on your GitHub repository:

    $ git push origin 2012-12-my-camp

and submit a pull request (the base branch should match your
`YYYY-MM-LOCATION` branch tag).  The base branch of your pull request
is irrelevant; GitHub doesn't allow you to explicitly request new
branches with pull requests.

After the pull request is accepted (which shouldn't take long, since
there shouldn't be any controversy over its content), the developer
who merged the pull request will tag the boot camp branch and delete
the branch itself

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

# <a id="tweaks" /> Tweaks and hints

The following notes provide helpful hints for managing your
repositories.  Feel free to skip them if they don't sound interesting.

## <a id="simple" /> Simplifying your local branch structure

If you don't like remote branches cluttering your local repo, you can
clone a single branch of the master repository using:

    $ git clone --single-branch https://github.com/YOU/boot-camps.git

You can also limit the branches you fetch from upstream.  After adding
the `swc` remote, run:

    $ git config remote.swc.fetch +refs/heads/master:refs/remotes/swc/master

After this, future calls to `git fetch` will retrieve only the
`master` branch from `swc` and its associated tags, ignoring other
branches and unrelated tags.

## <a id="disjoint" /> Disjoint branches

If you really want to roll your own content, feel free to skip the
master branch entirely.

    -o---o---o---o          swc/master
      \
       o---o                swc/git-wtk

             I---o---o---o  2012-12-my-camp

    Figure 5: A disjoint branch (2012-12-my-camp).  The commit “I”
    has no parents.  Different branches stored in the same repository
    don't need to share any common commits.  They're still addressing
    the same goal, and having them in the same repo means its easier to
    clone/fetch/diff/….

## <a id="hub" /> Avoiding the GitHub website

If you don't like forking and issusing pull requests from the GitHub
websites, you can use [hub][] to perform these operations from the
command line.  Hub is available as `dev-vcs/hub` in Evgeny Mandrikov's
`godin` overlay on [Gentoo][]; installation instructions for some
other platforms is available [in the README][hub-install].

Using `hub` to submit pull requests is similar to using Git's builtin
`request-pull` command, except that `hub` created pull requests on
GitHub, while `request-pull` prints a message onto stdout that should
be emailed to the maintainer.

### <a id="hub-clone" /> Cloning the master repository

    $ git clone https://github.com/swcarpentry/boot-camps.git
    $ cd boot-camps
    $ hub fork

This is the same as the hub-less procedure, except that the remote
names have changed.

    hub-less  hub     Repository URL
    ========  ======  ===========================================
    swc       origin  git://github.com/swcarpentry/boot-camps.git
    origin    YOU     git://github.com/YOU/boot-camps.git

You'll have to make appropriate adjustments to the other commands
(e.g. for creating a new boot camp, branch off from `origin/master`
instead of `swc/master`).

### <a id="hub-general" /> General content

Create your feature branch as described for hub-less development, but
after publishing to `YOU/feature-branch` you can create the pull
request using hub:

    $ hub pull-request

The pull request base defaults to the tracked branch and the head
defaults to the current branch, so you shouldn't need to specify
either explicitly.

### <a id="hub-archive" /> Post-boot-camp archival

After publishing your boot camp branch to `YOU/2012-12-my-camp`,
create a pull request using:

    $ hub pull-request 'tag completed 2012-12-my-camp' -b origin:master

As mentioned earlier, don't worry about having `master` as the base
branch.


[git-book]: http://git-scm.com/book/en/Git-Basics-Working-with-Remotes
[user-manual]: https://www.kernel.org/pub/software/scm/git/docs/user-manual.html#public-repositories
[gits]: http://lists.software-carpentry.org/listinfo.cgi/gits-software-carpentry.org
[IRC]: http://webchat.freenode.net/?channels=swcarpentry
[boot-camps]: https://github.com/swcarpentry/boot-camps
[gh-pull]: https://help.github.com/articles/using-pull-requests
[gh-account]: https://github.com/signup/free
[gh-fork]: https://help.github.com/articles/fork-a-repo
[https]: https://help.github.com/articles/set-up-git#password-caching
[ssh]: https://help.github.com/articles/generating-ssh-keys
[hub]: https://github.com/defunkt/hub
[Gentoo]: http://www.gentoo.org/
[hub-install]: https://github.com/defunkt/hub#installation
