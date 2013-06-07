This page just tells you what to do.  If you want an explanation of
each step, see [[the extended version|Workflow]].

# <a id="clone" /> Cloning the master repository

Log into GitHub, and [fork][gh-fork] the [boot-camps
repository][boot-camps].  Then:

    $ git clone https://github.com/YOU/boot-camps.git
    $ cd boot-camps
    $ git remote add swc https://github.com/swcarpentry/boot-camps.git
    $ git fetch swc

# <a id="new" /> Creating a new boot camp branch

    $ git checkout -b 2012-12-my-camp swc/master

# <a id="develop" /> Developing boot camp content

## <a id="camp-specific" /> Camp-specific content

    $ …hack commit hack commit hack commit…
    $ git push origin 2012-12-my-camp

## <a id="general" /> General content

Put general content in feature branches (e.g. `typo-fix`):

    $ git checkout -b typo-fix swc/master
    $ …hack commit hack commit hack commit…
    $ git push origin typo-fix
    $ git checkout 2012-12-my-camp
    $ git merge typo-fix

Make a [pull request][gh-pull] on GitHub to get your feature branch
merged upstream.  After the pull request is merged:

    $ git branch -d typo-fix
    $ git push origin :typo-fix

# <a id="archive" /> Post-boot-camp archival

    $ git push origin 2012-12-my-camp

Then submit a pull request asking for a tag.

[boot-camps]: https://github.com/swcarpentry/boot-camps
[gh-pull]: https://help.github.com/articles/using-pull-requests
[gh-fork]: https://help.github.com/articles/fork-a-repo
