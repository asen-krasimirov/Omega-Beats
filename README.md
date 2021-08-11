# Omega Beats
"Omega Beats" is a Django Web Application in which you can create and share music.

## Purpose
I made this project as part of Softuni's course "Python Web Framework- July 2021". To make it I utilized the knowledge I gained during the course. In it, I used techniques like template inheritance, using media and static files, authentication, CBVs, and more.

### Deployed to:
The application is deployed on Heroku here- https://omega-beats.herokuapp.com/

### Technologies used:
* Python 
* Django
* Javascript
* HTML
* CSS

## Project Description
### Registered Apps
1. common
2. beats
3. omega_beats_auth
#### common 
* Holds the home page view
* like/comment models and logic
#### beats
* Contains the main App data entity- the "Beat"
* also the BeatPlay and BeatNotes models
* Holds the browser page, beat details, beat player, and recorder
* All CRUD operations for the "Beat"
#### omega_beats_auth
* Contains the login/register functionality
* Holds the extended User and Profile model

### Authentication
The UserModel is extended and the login is made via email and password.<br>
The authentication logic is stored in the <b>omega_beats_auth</b> app.<br>
There are three types of users:
* Annonymus
* Authenticated
* Admins
### User Privilages:
#### Annonymus
These users are able to browse other user's creations, view their details, and listen to them.
#### Autenticated
These users have all the privileges of the anonymous users plus having the ability to like and comment on different beats.<br>
They can also create their own music and customize their own profile pages. They can edit and delete the content they make.
#### Admins
They have a special admin page where they can edit and delete other user's content.

### Storage
All profile and beat cover images are stored in Cloudinary Management Media Library. The images are called with cloudinary's API.