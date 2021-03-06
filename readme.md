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

<!-- User authenticate with Django QraphQL JWT -->
Go to https://github.com/flavors/django-graphql-jwt
1. Follow instructions on the README
2. Add Query in users/schema.py to get info from users for jwt auth etc. Query = 'me'
3. Resolve query, 'me'

<!-- Once get JWT, provide on Auth Header -->
*Need to use insomnia (insomnia.rest) as graphql does not provide this functionality

* Use JWT Token with insomnia to auth user
Provide the auth header from graphql into into Insomnia
--> JWT "token#"

<!-- Connecting Users with Tracks -->
* Link new tracks with users - we get info on who created a track. Thus, need to merge tracks & users models.
1. add 'posted_by' to Track model
2. Adding .ForeignKey() allows many to one functionality - e.g numerous tracks linked to 1 user. 
3. Use on_delete=models.CASCADE as it allows ALL tracks to be deleted if user deletes their profile. 
4. Makemigrations and migrate (whenever there is a change to a model)
5. Update Make Track Mutation in tracks/schema.py
--> when we create a track, we want info from the user.
--> get info from user in context and then pass into posted_by field. 
6. Create error handling for unauth'd users in tracks/schema.py

<!-- Update/Delete Track Functionality -->
Update & Delete Tracks
1. Got o tracks/schema.py and add class UpdateTrack
2. Ensure that we use posted_by field so that only the owner can U/D the track. 
3. Register mutation in base mutation class

4. Add Delete Tracks ability in schema.py
*Only return id of deleted track (other info is irrelevant)

<!-- Add ability to like tracks -->
1. Not going to create separate Like Model. Going to create Like class under Track class and modelled with class 'Like'.
2. MODEL STRUCTURE: Each track will have info of its likes and vice-versa. 
3. Make migrations
4. CREATE LIKES
- Import Like Model into app/schema.py and UserType from users/schema.py
- Add CreateLike Class in app/schema.py

<!-- Query for Likes -->
*Ability to see Likes on Tracks
* Get list of all likes and list of all tracks
* In app/schema.py
1. Create class LikeType in schema.py where inner meta class is modelled after the Like model.
2. Create likes Query - LikeType
3. Add resolver in root query class
4. Return Like.objects.all()

*Now when you query for likes in GraphiQL, you look for likes and the usernames/tracks attached to each like. 

<!-- Handling Errors with GraphQL -->
1. Move away from Raising exceptions to use class, GraphQL Error
2. Import into schema.py
3. Replace Exceptiion with GraphQLError

<!-- Search for tracks -->
* Search through all tracks through their id's, descip's etc.
1. In schema.py
2. Add search argument
3. Use icontains as search functions

<!-- FRONT-END -->
<!-- Material UI -->
- Utilised Material UI for basic front-end 
- Color themes are held in withRoot.js that injects theme with CssBaseline component and wrap around Root Component & Main Auth Component.
- Each Component also has separate Styles function with property names and each Component is exported whilst wrapped with the withStyles function. 

<!-- Structure -->
- Index.js is entry-point
- Root.js will handle routes (2 Main Routes) - 
  Pages\App.js (Root Route) and Pages/Profile.js 

- Every user will have a Profile route - /profile/:userid
- Register & Login Page (not sperate route, just prevents   users from seeing home page).

AUTHENTICATION:
- Auth/Login & Register.js

SHARED (Across )
- Header, Error, Loading and AUDIO PLAYER components!

TRACK FOLDER
- All Components for CRUD, Searching, Likes etc.
- Link to back-end functionality through each component. 

<!-- APOLLO BOOSTER -->
1. Use Apollo Boost to execute queries & mutations from React App
- Use Apollo when utilising GraphQL & React.js

2. Connecting back-end to React-client
- in src/index.js

<!-- Allow cross-origin access from our React App to our Django Back-end -->
3. Utilise djagno-cors-headers to allow cross-origin resource sharing between Django and React
- look on github.com/ottoylu/django-cors-headers
- Install cors-headers to DJANGO INSTALLED APPS
- Install Middleware as well (at the top)
- Add CORS_ORIGINS_WHITELIST

<!-- AUTHENTICATING USERS -->
* In Auth/
*STRUCTURE 
When user visits 1st, shown Register page. Once logged-in, we give them valid JWT - we verify and then send to home page. 

Within index.js - display <Root /> component IF AUTHENTICATED.

If NOT AUTHENITCATED, display <Auth />> Component which holds Register or Login form

1. <Auth /> Component for index.js

2. Display Regiser/Login form on Auth Component to /index.js

3. Implement Register & Login Forms on respective components
- When a user fills out the form and usbmit, want to execute a Create New User execution with mutation CreateUser - thus, bring in Mutation component to React Apollo. 
4. Import gql from apollo-boost as well. 

<!-- *Set values to State* -->
When a user inputs a value to a field, we will set it in state:
onChange={event => setUsername(event.target.value)}
The onChange handler - stores the value of the username etc. into state

5. Complete <Success Dialog> in Register.js - for UI, after Registration. 

<!-- LOGIN after registration -->
Handle Login submission, after Registration through Auth/index.js
- Create State and allow users within Register component or Login component see the login or not. 

<!-- Error Handling -->
Via error.js

6. Finalise Login Form
- Utilise similar code as Register.js and use tokenAuth mutation for Login function.
- Complete Login form

<!-- Login (JWT Handling) -->
7. Apollo Client State to Manage Auth State
- When users login, we use tokenAuth mutation and get JWT back.
- We use this to auth users and kick them to Home page and then provide JWT on all future requests.
i. Thus, store JWT in browser via local storage - /Login.js
ii. Also use JWT on all future requests

iii. Store authToken in Global state to ensure authToken is constant throughout page refreshes etc.
- ApolloBoost has built-in state management system (src/index.js) - clientState
- !!isLoggedIn - grabs the authToken in localStorage and if there is 'something' there, then the '!!' converts that to a boolean. 
- In index.js - If isLoggedIn is true, then show the Root Component and if UnAuthenticated, then show the Auth Componenent

<!-- Add JWT to Authorization Header with Apollo Client -->
*Send authToken to backend as Auth Header in a request

1. In index.js - add fetchOptions
2. Include credentials
3. Ensure token is kept in the header and if empty, then make a empty string.

<!-- Routing - React Router 4 -->
/Root.js - import router settings
1. Build Routes in Root.js
2. Then Logo and user info for routing
- Add Header.js with routing
- Add Signout function - Auth/Signout.js
*Logo goes to "/" and Username goes to Profile page

3. Signout Button - "click" the Signout button
- Remove authToken from localStorage
- Amend isLoggedIn to False
- /Signout.js - interact with Client without Mutation or Query is to import a different component - Apollo Consumer

<!-- Add Loading and Error Component -->
Added to Root.js and linked to Error.js & Loading.js

<!-- Content Area of Home Page -->
1. Search bar at top - for tracks
2. Track List area of tracks user created
3. Can Like the track, see the track details, play the track and if user has created the track - can delete it.
4. Floating button on bottom right and allow auth'd users to create new trackss
*ALL IN Pages/App.js

i. TRACKLIST
Use the Query_Tracks and display user's tracks on the home page (TRACKLIST)
- Input Expansion Panel settings
- Place 4 COMPONENTS WITHIN TrackList 
  a. UpdateTrack
  b. LikeTrack
  c. DeleteTrack
  d. AudioPlayer

<!-- Build CreateTrack Button & Dialog -->
- CreateTrack.js
- Within <> React Component - add floating button
- Add Create Track FormField

<!-- Cancel Functionality, Audio File Description & Add Track Functionality -->
* Also ensure that users can submit audio files only
CreateTrack.js
- Toggle Dialog - Create Open Piece of State
  a. Set Dialog state to Open after click and false, when clicking 'Cancel'.
  b. Add button (floating button) must disappear when CreateTrack dialog is open. Thus, clearIcon when open is True.
  c. Size of description text field - multi-line - FormControl component
  d. Audio file name - FormControl
  - But first need to accept valid audio file types

  <!-- Upload files functionality -->
  * Use service called Cloudinary
  CreateTrack.js

  <!-- Refresh Page after upload -->
  * Use refetchQueries

  <!-- Clear Dialog State after upload -->
  CreateTrack.js
  Make a controlled by state component

  <!-- Create File Size Limit -->
 *CreateTrack.js - in handleAudioChange

 <!-- Audio Player Functionality -->
 * in shared/AuidoPlayer.js
 - Use component from react player library
 Passed url of track into AudioPlayer.js
 And linked url in TrackList - url={track.url} (AudioPlayer Component!)

 <!-- Search Tracks Function -->
 Search Query - title, username of poster, description etc.
 *Searchracks.js
 Need to conditionally execute a query - use apollo-consumer component in order to get access to client and execute a query from it.
 *In SearchTracks.js
 - Wrap form in ApolloConsumer tags
 - Add function and put form into the return function

<!-- Update TrackList to Search Query -->
Create New State in App.js
* Override data that gets passed to TracksList, based on Search Query. In App Component - determine if we have any hits on a search or not.

* Clear search and results
- Click on the Clear (X) button
clearSearchInput - call and pass empty array
call setSearch and clear input - make controlled component - input will be cleared
- FOCUS the Search Input - add prop inputRef={inputEl} and use React Hook (useRef) where its return element focuses/highlights. 

<!-- Update Track and Delete Track Components - FULL CRUD -->
*UPDATE TRACK
1. Create button in updatetrack.js
- Need Track info pre-filled upon update track
- Only allow owner to update track
- Compare current user to OP (ID to ID) - UpdateTrack.js
- Avoid passing user data down through multiple levels of props - RATHER USE - react context! Allows to pass data/state down the component tree and not touch irrelevant components.
a. Start in root.js
b. UpdateTrack.js - place in currentUser state

<!-- Delete Track -->
* Need to ensure it is the OP
* DeleteTracks.js
- Ensure refresh list after deletion

<!-- Likes/ Liking Tracks -->
1. Create Button
2. Add Like Mutation
3. Prevent users from liking a track multiple times

DATA it needs: 
need to know track id
display the like count of track

Disable Like for own user 
- Grab current user's like set, go through array and see in sub-field if there is an id that matches a track id in list. 
- UserContext
- In IconButton - handleDisableLikedTrack
