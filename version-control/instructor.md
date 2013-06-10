Version control is the most important practical skill we introduce.
as the last paragraph of the introduction above says, the workflow
matters more than the ins and outs of any particular tool.  By the end
of 90 minutes, the instructor should be able to get learners to chant,
"Update, edit, merge, commit," in unison, and have them understand
what those terms mean and why that's a good way to structure their
working day.

Provided there aren't network problems, this entire lesson can be
covered in 90 minutes.  The example at the end showing how to use
Subversion keywords to track provenance is the "ah ha!" moment for
many learners.  If time is short, skip the material on recovering old
versions of files in order to get to this section instead.  (The fact
that provenance is harder in Git, both mechanically and conceptually,
is one reason to keep teaching Subversion.)

Prerequisites
-------------

* Basic shell concepts and skills (`ls`, `cd`, `mkdir`, editing
  files).
* Basic shell scripting (for the discussion of provenance).

Teaching notes
--------------

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

* Version control is typically taught after the shell, so collect
  learners' names during that session and create a repository for them
  to share with their names as both their IDs and their passwords.
  The easiest way to create the repository is to use a server managed
  by an ISP such as Dreamhost, or on SourceForge, Google Code, or some
  other "forge" site, all of which provide web interfaces for
  repository creation and management.  If your learners are advanced
  enough to be using SSH, you can instead create it on any server they
  can access, and connect with the `svn+ssh` protocol instead of
  HTTPS.

* Be very clear what files learners are to edit and what user IDs they
  are to use when giving instructions.  It is common for them to edit
  the instructor's biography, or to use the instructor's user ID and
  password when committing.  Be equally clear *when* they are to edit
  things: it's also common for someone to edit the file the instructor
  is editing and commit changes while the instructor is explaining
  what's going on, so that a conflict occurs when the instructor comes
  to commit the file.

* Learners could do most exercises with repositories on their own
  machines, but it's hard for them to see how version control helps
  collaboration unless they're sharing a repository with other
  learners.  In particular, showing learners who changed what using
  `svn blame` is only compelling if a file has been edited by at least
  two people.

* If some learners are using Windows, there will inevitably be issues
  merging files with different line endings.  `svn diff -x -w` is
  supposed to suppress differences in whitespace, but we have found
  that it doesn't always work as advertised.
