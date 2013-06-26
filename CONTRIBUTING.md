Contributing Boot Camp Material
===============================

Licenses
--------

See http://software-carpentry.org/license.html for the licenses covering
Software Carpentry material. By contributing you are agreeing that
Software Carpentry may redistribute your work under these licenses.

Workflow
--------

Software Carpentry uses a development workflow similar to that of
[AstroPy][] and many other open source projects.  See our [workflow
docs][workflow] for details.

### Maintainers

The boot-camps repository covers a large range of material.  To focus
limited developer time, we have subsystem maintainers who are
responsible for keeping particular sections up to date.  If you submit
a pull request touching a subsystem, you should ping the maintainer in
your pull request message, to let them know that they should review it
for merging.

* contributing: [wking][] (but let me know if you want to take over)
* version-control/git: [wking][] (but let me know if you want to take over)
* version-control/svn: unmaintained

It's also considerate to prefix your commit messages and pull requests
with at least the subject/tool to help others who are interested in
the topic easily locate changes that they might be interested in
reviewing.  For example:

    version-control/git/README.md: Add paragraph pitching Git

File Formats
------------

### Text

Text documents should be in [Markdown][] format and compatible
with [Redcarpet][], the engine GitHub uses to render Markdown.

### Slides

The preferred format for slide presentations is still to be determined.

[AstroPy]: http://astropy.readthedocs.org/en/latest/development/workflow/development_workflow.html
[workflow]: contributing/README.md
[Markdown]: http://daringfireball.net/projects/markdown/
[Redcarpet]: https://github.com/vmg/redcarpet

[wking]: https://github.com/wking
