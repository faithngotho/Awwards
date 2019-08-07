PRORATE
Created bY
William Mango 05/08/19

Description
The application allows a user to post a project he/she has created and get it reviewed by his/her peers and other users.

User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:

View posted projects and their details
Post a project to be rated/reviewed
Rate/ review other users' projects
Search for projects
View projects overall score
View my profile page
BDD
Behaviour	Input	Output
Display all projects	signup & login	a list of projects
To search project	project title	project and its objects
add a project	project instances	new project
create profile	your details	new profile
view your profile	click on fa-user nav icon	your profile/projects
rate a project	click on project title	rating page
SetUp / Installation Requirements
Prerequisites
python3.6
pip
virtualenv
Requirements.txt
Cloning
In your terminal:
$ git clone https://github.com/mangowilliam/prorate $ cd instagram2

Running the Application
Creating the virtual environment
$ python3.6 -m venv --without-pip virtual $ source virtual/bin/activate $ curl https://bootstrap.pypa.io/get-pip.py | python

Installing Django and other Modules
$ see Requirements.txt

To run the application, in your terminal:
$ python3.6 manage.py runserver #Testing the Application To run the tests for the class files:

$ python3.6 manage.py test images

Technologies Used
Python3.6 Django and postgresql

Support and contact details
contact faithwangari248@gmail.com for any kind of support.

Live Link
click here

License
MIT licence Copyright (c) 2019 faithngotho
