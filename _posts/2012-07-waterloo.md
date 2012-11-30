{% extends "_bootcamp.html" %} {% block file_metadata %}  {% endblock
file_metadata %} {% block content %}

data1.txt

    
    Date,Species,Count
    2012-07-01,squirrel,23
    2012-07-01,goose,9
    2012-07-01,raccoon,4
    2012-07-02,squirrel,14
    2012-07-02,skunk,1
    2012-07-03,goose,5
    2012-07-03,bat,1

data2.txt

    
    Date,Species,Count
    2012-07-01,squirrel,15
    2012-07-01,goose,5
    2012-07-01,raccoon,1
    2012-07-02,squirrel,10
    2012-07-03,goose,5
    2012-07-03,raccoon,1

**Where:** Davis Centre DC 1568, University of Waterloo, 200 University Avenue West, Waterloo, Ontario.

**When:** July 12-13, 2012. We will start at 9:00 and end at 4:30 each day.

{% include "_what.html" %} {% include "_who.html" %} {% include
"_requirements.html" %} {% include "_content.html" %} {% include
"_contact.html" %} {{eventbrite(page.eventbrite_key, page.venue, page.date)}}
{% endblock content %}

