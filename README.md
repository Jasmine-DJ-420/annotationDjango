# annotationDjango
An annotation tool using Django Framework.

Using `python manage.py runserver 0.0.0.0:8000` to start server.

Then `http://127.0.0.1:8000/admin/` could be used to manage users, 

and `http://127.0.0.1:8000/labeling` is where one should start annotating.

The texts waiting to be labeled should be imported into Table labeling.issuetext, and the annotators' information should be saved 
into Table labeling.users.
