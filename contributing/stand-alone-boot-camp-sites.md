Warning: the following workflows use Git's [submodule][] command ([Pro
Git chapter][pg-submodules]).  This isn't really very difficult, but
if you're still struggling to wrap your head around the whole “branch”
concept, you're probably better off [developing your site in the
gh-pages branch][boot-camp-pages].

Sometimes you want more than Jekyll can offer, or you want to keep the
source for your website in its own branch, away from the other stuff
in `gh-pages`.  If your page content is living in a branch called
`2013-01-chicago.jekyll`, here's how you would tie it into the master
`gh-pages`.

# Add a new boot camp

Check out your website branch into a subdirectory:

    $ git checkout gh-pages
    $ git submodule add -b 2013-01-chicago.jekyll ./ 2013-01-12-chicago

Commit your changes:

    $ git commit -am '2013-01-chicago: add boot camp submodule'

Make sure that your branch exists in the public repository, otherwise
users (like [GitHub's Pages generator][pages-submodule]) will be able
to check it out:

    $ git push swc gh-pages 2013-01-chicago.jekyll

This line pushes your recent `gh-pages` commit as well as your
`2013-01-chicago.jekyll` branch.

# Setting up submodules on a new checkout

When you checkout this branch, it will have a `.gitmodules` file and
empty module directories.  To initialize the submodule metadata and
checkout the submodule content, you'll need to run:

    $ git submodule update --init

After you've initialized the submodules once (which marks them as
interesting in your local `.git/config`), you can just run:

    $ git submodule update

on future checkouts.

# Maintenance

After hacking away at your website branch, you'll want to update the
submodule in `gh-pages` to publish your updates.  Checkout the branch:

    $ git checkout gh-pages

And update to your current branch tip:

    $ git submodule update --remote 2013-01-12-chicago

You can update all the submodules to their current branch tips with:

    $ git submodule update --remote

but you'll probably want to limit your changes to your own boot camps
to avoid pulling someone else's work in progress.

The `--remote` option requires Git version 1.8.2 or later.  If you are
running an earlier version, it's probably easiest to change into the
boot camp directory and merge directly:

    $ cd 2013-01-12-chicago
    $ git pull

Commit your changes and push:

    $ git commit -am '2013-01-12-chicago: Update following upstream development'
    $ git push swc gh-pages 2013-01-chicago.jekyll

# Archival

After the boot camp is over, you can replace your boot camp branch
with a tag.  For more detail, see the [Post-boot-camp archival
section][archive] of the [suggested Git workflow][workflow].

# Other generators

If you are using a non-Jekyll site generator, create a new branch
holding your site source, and another branch to hold your compiled
site.  Make the compiled branch a submodule of both the `gh-pages`
branch and your site source branch.  Setup would look something like:

    $ git checkout --orphan my-site-compiled
    $ git rm -rf .                   # clean up orphan index
    $ git commit --allow-empty -m 'Compiled version of my-site'
    $ git checkout my-site
    $ git submodule add -b my-site-compiled ./ build
    $ git config -f .git/modules/build/config push.default current
    $ git commit -am "build: Attach 'my-site-compiled' branch"
    $ git checkout gh-pages
    $ git submodule add -b my-site-compiled ./ 2013-01-06-my-site
    $ git commit -am "2013-01-06-my-site: Attach 'my-site-compiled' branch"

Update with something like the following:

    $ git checkout my-site
    $ make                           # or whatever, writes to `build/`
    $ cd build
    $ git add .
    $ git commit -am 'Compile my-site'
    $ git push
    $ cd ..
    $ git commit -am 'build: Compile'      # optional
    $ git checkout gh-pages
    $ git submodule update --remote 2013-01-06-my-site
    $ git commit -am '2013-01-06-my-site: Update following upstream development'
    $ git push swc gh-pages 2013-01-chicago.jekyll

For bonus points, tweak your build system to automatically perform
the Git manipulations for you:

    $ git checkout my-site
    $ make
    …confirm that the output makes sense…
    $ make push


[submodule]: http://www.kernel.org/pub/software/scm/git/docs/git-submodule.html
[pg-submodules]: http://git-scm.com/book/en/Git-Tools-Submodules
[boot-camp-pages]: boot-camp-pages.md
[pages-submodule]: https://help.github.com/articles/using-submodules-with-pages
[archive]: workflow.md#archive
[workflow]: workflow.md
