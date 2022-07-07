# Lab 28: Django CRUD and Forms

## Overview

Add full CRUD functionality to your bag of tricks by building a Django project that allows Creating, Reading, Updating and Deleting.

## Feature Tasks

Create web site in Django with 2 pages

- Create snacks_crud_project Django project
- Create snacks app
- Create Snack model
  - title field
  - purchaser field
  - description field
  - Register model with admin
- Create SnackListView that extends appropriate generic view
  - associated url path is an empty string
- Create SnackDetailView that extends appropriate generic view
  - associated url path is <int:pk>/
- Create SnackCreateView that extends appropriate generic view
  - associated url path is create/
- Create SnackUpdateView that extends appropriate generic view
  - associated url path is <int:pk>/update/
- Create SnackDeleteView that extends appropriate generic view
  - associated url path is <int:pk>/delete/
- Add urls to support all views, with appropriate names
- Add templates to support all views
- Add navigation links in appropriate locations to access all pages
- Make all necessary changes to project level files for project to run
  - In other words, make it work

### Setup

1. Create a virtual environment --> python –m venv .venv
2. Activate the virtual environment --> source .venv/bin/activate (for Linux and MacOS); .\.venv\Scripts\activate (for Windows)
3. Install Django --> pip install django
4. Create and start a Django project --> django-admin startproject djangho_snack_tracker_project .
5. Set up migrations --> python manage.py migrate
6. Run development server --> python manage.py runserver
7. Create a Django app --> python manage.py startapp snacks
8. Need to complete 3 steps before making migrations: TUV --> (1) templates (folder with base.html), (2) urls (in snacks folder), and (3) views(in snacks folder)
9. Make and apply migrations --> python manage.py makemigrations snacks
10. Apply the migrations --> python manage.py runserver
11. Create a super user as the administator of the site --> python manage.py createsuperuser
# username: admin
# email address: admin@admin.com
# password: admin
12. Test that the TUV and migrations worked in the development server
13. Add /admin to the end of the local host url to log in with the admin credentials
14. Update: add /1/update to the end of the local host to see the first item after it's been updated
15. Delete: add /delete to the end of the local host to see the deleted item is gone

### Tests

python manage.py test
