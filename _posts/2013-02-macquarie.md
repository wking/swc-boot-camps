{% extends "_bootcamp.html" %} {% block file_metadata %}  {% endblock
file_metadata %} {% block content %}

**Where:** Macquarie University, Sydney.

**When:** February 7-8, 2013. We will start at 9:00 and end at 4:30 each day.

{% include "_what.html" %} {% include "_who.html" %} {% include
"_requirements.html" %} {% include "_content.html" %} {% include
"_contact.html" %} {{eventbrite(page.eventbrite_key, page.venue, page.date)}}
{% endblock content %}

