In addition to the generic version control notes.

The example at the end showing how to use Subversion keywords to track
provenance is the "ah ha!" moment for many learners.  If time is
short, skip the material on recovering old versions of files in order
to get to this section instead.  (The fact that provenance is harder
in Git, both mechanically and conceptually, is one reason to keep
teaching Subversion.)

Teaching notes
--------------

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

* If some learners are using Windows, there will inevitably be issues
  merging files with different line endings.  `svn diff -x -w` is
  supposed to suppress differences in whitespace, but we have found
  that it doesn't always work as advertised.
