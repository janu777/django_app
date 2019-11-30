<!-- # django_app
About:
Django is a framework that uses python and doesn't rely on external libraries or packages for website building.

Django Documentation: https://www.djangoproject.com/

Structure:
1) Django is a single project with sepearate apps for each function. 
2) For example:
A django app like instagram may contain:
	a) User management: Login, logout, register and so on
	b) The image feed: Uploading, editing, and displaying images.
	c) Private messaging: Private messages between users and notifications 
all of these are different functionalities which will be different apps inside a django project.
3) A project will have common configurations like project settings, URLs, shared templates and static files. And each app can have its own database and its own function to control how the data is displayed to the user in HTML templates. Also each app has its oen HTML templates and static files like JavaScript and CSS. 
4) Django supports Model-View-Controller pattern a logic on which most web frameworks are built. 
5) SO, in each app there are three seperate files that handle the three main pieces of logic seperately:
* Model - base layer of an application. defines the datastructure. contains the database.

* View - display some or all of the data to the user with HTML and CSS

* Controller - handles how the database and the view interact. 
6) In django, the controller part is handled by django itself.


Create App:
1) create a repo
2) create a venv to easily deal with the dependecies
3) once you are inside the venv install django with pip isntall django.
4) use django-admin startproject "project name" to create a django project.
5) To run the server run python mange.py runserver to run the site locally
6) To create an app inside the project do python mange.py startapp "appname"

About app:
Contains
1) __init__.py tells python to treat file as a python package
2) admin.py contains settings for the django admin pages
3) apps.py contains settings for the application configuration 
4) models.py contains a series of classes that django's ORM converts to database tables.
5) tests.py contains test classes.
6) views.py contains functions and classes that handle what data is displayed in the HTML templates.  

Once the app has been created it needs to be installed in the project. add the created app to settings inside the project name

Inside view.py in apps create a function that can take a htmlrequest as input and load the html page
create folder templates/ inside the app and create the html file

Now final step is to link the url with the app.
inside the urls.py the path needs to be imported and create a list of url patterns that correspond to each view function.
 -->