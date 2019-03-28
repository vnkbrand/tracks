1. Setup Pipenv
2. Install Dependencies - install django graphene-django django-graphql-jwt django-cors-headers
3. Install --dev autopep8 (code formatter)
4. Setup Django - django-admin start project app

<!-- Create Database -->
1. cd into app
2. migrate DB - python manage.py migrate
3. Then you have db.sqlite3 file in /app

<!-- Startup Server -->
1. python manage.py runserver

<!-- Begin App Dev -->
1. python manage.py startapp tracks
* Want the 'tracks' folder next to manage.py

<!-- Shape of track data - how to model tracks -->
1. In app/models.py - create tracks tracks' model
2. Link model in settings.py
3. Create migration file - make migrations. Take model from tracks app and then allow us to interact with DB - based on model. 
<!-- Ran migrations to update according to track model -->
4. Run python manage.py migrate

<!-- Create Data without admin panel -->
1. Use Django shell
2. *Within app folder --> python manage.py shell
3. from tracks.models import Track
4. ADD TRACKS TO DATA: 
*Track.objects.create( pass in values - Title etc.)
--> 
Track.objects.create(title="Track 1", description="Track 1 Description", url="https://track1.com")
5. Bring in graphene.django to query for these tracks
--> In app/settings.py - reference graphene.
6. Create schema.py file in tracks app

<!-- Add Graphql -->
Add Schema and URL /graphql/

*Now you can query for tracks in localhost/graphql

<!-- Add mutations for tracks -->
1. Go to tracks/schema.py
2. Add class "CreateTrack"
3. Add 2 Classes: graphene.ObjectType & graphene.Mutation

<!-- Add anther Mutation Class -->
1. Go to app/Schema.py
2. Create class Mutation

* Now you can add tracks in localhost/graphql

<!-- Create new users -->
1. Create users folder and users/scheema.py
* 2 Functions only
i. Add user through graphql mutation
ii. Query for individual user based on id (django gives django user model)
*from django.contrib.auth import get_user_model
2. import users.schema into app/schema.py

<!-- Create Query User based on their id -->
/users/schema.py
1. Create Query class
2. Enable Query in app/schema.py