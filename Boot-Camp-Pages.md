The [gh-pages branch][gh-pages] of the [boot-camps repo][boot-camps] is available for making web pages for particular boot camps. We use GitHub Pages' built-in [Jekyll][] rendering.

# About Jekyll and GitHub Pages

[Jekyll][] is a static site generator. It simplifies the process of web page creating by allowing you to base your page on a template and write just the content without worrying about headers. You can even write your pages in [Markdown][] so you don't have to worry about HTML at all, though if you want to work in HTML that's fine too. You can even skip the templates entirely and give Jekyll fully formed HTML files, Jekyll will just leave those alone.

[GitHub Pages][pages] are a way for us to publish web pages via GitHub. On any repository you can push content to a branch called `gh-pages` and GitHub will run that content through Jekyll and publish it on the web at a URL like `http://account-name.github.com/repo-name/`.

# Markup Languages

Any `.md`, `.markdown`, or `.html` file with a YAML block at the top (described below) is converty by Jekyll into standard HTML. Jekyll uses [Maruku][] to process the Markdown so you can use any syntax supported by Maruku.

# Boot Camp Pages Templates

We've set up the [gh-pages branch][gh-pages] of the [boot-camps repo][boot-camps] with a Jekyll framework and two initial templates:

* `base`: matches the style of http://software-carpentry.org
* `bare-bootstrap`: purely the defaults of [Bootstrap][]

Both templates include full access to [Bootstrap][] CSS and JavaScript libraries and have [Disqus][] comments enabled.

# YAML Front Matter

Jekyll will only process files that have a YAML block at the top. The YAML is where you specify a template you'd like to use and other metadata for the file. The most basic YAML block you should use will look something like this:

    ---
    layout: base
    title: My Page
    ---

That tells Jekyll to use the `base` template and sets the metadata `title` of your page, which the base template uses to set the title of the resulting HTML document.

# Syntax Highlighting

If writing your pages in Markdown you can turn on syntax highlighting of code blocks using a [Jekyll extension][extensions] to the Liquid template language. Simple wrap your code block like so:

    {% highlight python %}
    print "What's up, doc?"
    {% endhighlight %}

The language specifier can be any "short name" for the [available lexers in Pygments][lexers].

# Instructions for Making Pages


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
