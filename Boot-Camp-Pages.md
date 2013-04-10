The [gh-pages branch][gh-pages] of the [boot-camps repo][boot-camps] is available for making web pages for particular boot camps. We use GitHub Pages' built-in [Jekyll][] rendering.

This wiki page covers simple Jekyll-rendered boot camp pages.  You can also compile a website using another generator and easily include its output in the `gh-pages` branch using Git submodules.  This workflow is discussed [[here|Stand-Alone-Boot-Camp-Sites]].

# <a id="jekyll" /> About Jekyll and GitHub Pages

[Jekyll][] is a static site generator. It simplifies the process of web page creating by allowing you to base your page on a template and write just the content without worrying about headers. You can even write your pages in [Markdown][] so you don't have to worry about HTML at all, though if you want to work in HTML that's fine too. You can even skip the templates entirely and give Jekyll fully formed HTML files, Jekyll will just leave those alone.

[GitHub Pages][pages] are a way for us to publish web pages via GitHub. On any repository you can push content to a branch called `gh-pages` and GitHub will run that content through Jekyll and publish it on the web at a URL like `http://account-name.github.com/repo-name/`.

# <a id="markup" /> Markup Languages

Any `.md`, `.markdown`, or `.html` file with a YAML block at the top (described below) is converted by Jekyll into standard HTML. Jekyll uses [Maruku][] to process the Markdown so you can use any syntax supported by Maruku.

# <a id="template" /> Boot Camp Pages Templates

We've set up the [gh-pages branch][gh-pages] of the [boot-camps repo][boot-camps] with a Jekyll framework and two initial templates:

* `base`: matches the style of http://software-carpentry.org
* `bare-bootstrap`: purely the defaults of [Bootstrap][]

Both templates include full access to [Bootstrap][] CSS and JavaScript libraries and have [Disqus][] comments enabled.

# <a id="yaml-front-matter" /> YAML Front Matter

Jekyll will only process files (Markdown or HTML) that have a YAML block at the top. Files which do not contain YAML front matter are included in your site but never modified by Jekyll. The YAML is where you specify a template you'd like to use and other metadata for the file. The most basic YAML block you should use will look something like this:

    ---
    root: ..
    layout: base
    title: My Page
    ---

That tells Jekyll to use the `base` template and sets the metadata `title` of your page, which the base template uses to set the title of the resulting HTML document.  `root` gives the relative URL from your page (e.g. `http://swcarpentry.github.com/boot-camps/2013-01-12-chicago/`) to the website root (`http://swcarpentry.github.com/boot-camps/`), which the templates use when linking to CSS and other auxiliary files.

Note that the value for `root` should be determined relative to a page's URL, not the page's source path.  The file path will have an extra `_posts/` directory that disappears during the Jekyll compilation so that `_posts/2013-01-12-chicago/index.html` will become `http://swcarpentry.github.com/boot-camps/2013-01-12-chicago/index.html`.

# <a id="syntax-highlighting" /> Syntax Highlighting

When writing your pages using the provided templates you can turn on syntax highlighting of code blocks using a [Jekyll extension][extensions] to the Liquid template language. Simply wrap your code block like so:

    {% highlight python %}
    print "What's up, doc?"
    {% endhighlight %}

The language specifier can be any "short name" for the
[available lexers in Pygments][lexers].

# <a id="pages" /> Instructions for Making Pages

These instructions describe a workflow that incorporates some of the best practices advocated by Software Carpentry.

## <a id="checkout" /> 0. Checkout the `gh-pages` branch

    cd boot-camps
    git checkout gh-pages

## <a id="branch" /> 1. Checkout a new branch for your changes

Make a branch in your repo based on the `gh-pages` branch that will hold a set of changes

    git checkout -b my-boot-camp-changes gh-pages

## <a id="naming" /> 2. Make a directory for the boot camp

By convention and for compatibility with Jekyll your directory name will be in the form `YYYY-MM-DD-venue`. To figure out the directory name go to the [Software Carpentry boot camps directory][swc-bootcamps] and find the page for your boot camp. It should have a URL something like http://software-carpentry.org/bootcamps/2013-01-chicago.html. In the file name at the end is the short designation for your boot camp, in this case `2013-01-chicago`.

That's not quite the name of the directory, though. For compatibility with Jekyll the name must also include a day number. Add in the date of the first day of the boot camp so that, for example, `2013-01-chicago` becomes `2013-01-12-chicago`.

Finally, make a new directory with this name in the `_posts` directory:

    cd boot-camps
    mkdir _posts/YYYY-MM-DD-venue

## <a id="content" /> 3. Add content

Your boot camp directory should probably have at least an `index.md` or `index.html` file, but the site design is up to you. Remember that Jekyll will only process files that contain YAML front matter, as described above.

## <a id="testing" /> 4. Test your changes

In order to ensure that your changes render appropriately, you can [process them locally with Jekyll][gh-pages-jekyll].  If you already have Jekyll installed, then this may be sufficient:

    jekyll --pygments --no-lsi --safe

## <a id="push" /> 5. Push your new branch

Once you are happy that your changes are correct, push the new branch to the repo.  This may depend on whether you are pushing to the main Software Carpentry repo or you are planning to use your own.

    git push origin my-boot-camp-changes

## <a id="pull_request" /> 6. Issue a pull request

On github, find your branch and issue a pull request from this branch to the gh-pages branch, with comments/guidance for a potential reviewer.  Another user can then review your changes and merge your pull request when satisfied.

# <a id="example" /> Example Pages

To save time creating pages it may be helpful to copy existing pages in the `_posts` directory. The directory `1900-01-01-example-page` contains purely example material, and the directory `2012-10-23-caltech` contains an [example](http://swcarpentry.github.com/boot-camps/2012-10-23-caltech/) of a highly customized HTML page used for a 2012 boot camp.

[gh-pages]: https://github.com/swcarpentry/boot-camps/tree/gh-pages
[boot-camps]: https://github.com/swcarpentry/boot-camps
[Jekyll]: http://jekyllrb.com/
[Markdown]: http://daringfireball.net/projects/markdown/
[pages]: http://pages.github.com
[Maruku]: http://maruku.rubyforge.org/
[Bootstrap]: http://twitter.github.com/bootstrap/
[Disqus]: http://disqus.com/
[extensions]: https://github.com/mojombo/jekyll/wiki/Liquid-Extensions
[lexers]: http://pygments.org/docs/lexers/
[swc-bootcamps]: http://software-carpentry.org/bootcamps/
[gh-pages-jekyll]: https://help.github.com/articles/using-jekyll-with-pages