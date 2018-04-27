# annotationDjango
An annotation tool using Django Framework.

Using `python manage.py runserver 0.0.0.0:8000` to start server.

Then `http://127.0.0.1:8000/admin/` could be used to manage users, 

and `http://127.0.0.1:8000/labeling` is where one should start annotating.

The texts waiting to be labeled should be imported into Table labeling.issuetext, and the annotators' information should be saved 
into Table labeling.users.

## To use SentiSW for a publication, please cite the following paper: 

Jin Ding, Hailong Sun, Xu Wang and Xudong Liu. Entity-level sentiment analysis of issue comments. The 3rd International Workshop on Emotion Awareness in Software Engineering (SEmotion), 2018. (accepted).
