Version control is the most important practical skill we introduce.
By the end of 90 minutes, the instructor should be able to get
learners to fetch upstream updates, make local edits, and submit their
changes upstream and why that's a good way to structure development.

Provided there aren't network problems, this entire lesson can be
covered in 90 minutes.

Tool choices
============

There are many version control tools available, and we have Software
Carpentry branches for some of them.  Possible choices:

Git
---

* `git://github.com/wking/swc-boot-camps.git version-control-git`

Subversion
----------

* `git://github.com/wking/swc-boot-camps.git version-control-svn`

Teaching notes
==============

* Make sure the network is working *before* starting this lesson.

* Give learners a ten-minute overview of what version control does for
  them before diving into the watch-and-do practicals.  Most of them
  will have tried to co-author papers by emailing files back and
  forth, or will have biked into the office only to realize that the
  USB key with last night's work is still on the kitchen table.
  Instructors can also make jokes about directories with names like
  "final version", "final version revised", "final version with
  reviewer three's corrections", "really final version", and, "come on
  this really has to be the last version" to motivate version control
  as a better way to collaborate and as a better way to back work up.

* Learners could do most exercises with repositories on their own
  machines, but it's hard for them to see how version control helps
  collaboration unless they're sharing a repository with other
  learners.  In particular, showing learners who changed what using
  `blame` is only compelling if a file has been edited by at least two
  people.
