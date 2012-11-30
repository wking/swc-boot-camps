{% extends "_bootcamp.html" %} {% block file_metadata %}  {% endblock
file_metadata %} {% block content %}

**Where:** University of Waterloo, Engineering 6 building, room 4022 [[map](https://uwaterloo.ca/map/)]

**When:** January 12-13, 2013. We will start at 9:00 and end at 4:30 each day.

{% include "_what.html" %} {% include "_who.html" %} {% include
"_requirements.html" %}

**Content:** ****The syllabus for this boot camp will include:

  * using the shell to do more in less time
  * using version control to manage and share information
  * basic Python programming
  * how (and how much) to test programs
  * Scientific Python, manipulation of arrays, matrices, and plotting data
{% include "_contact.html" %} {{eventbrite(page.eventbrite_key, page.venue,
page.date)}} {% endblock content %}

