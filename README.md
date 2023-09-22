# Django_Crud
Learning backend using Django. Creating CRUD operation using Django . 



# How to do initial setup -> 
=== Initial setup =================================================================================================================
1. python -m venv env       // for creating the virtual environment
2. env/Script/activate     // activate virtual enironment
3. create a new folder and cd newforder 
4. pip install djangorestframework     // run command inside the newfolder
5. django-admin startproject main .   // command for initiallization of new project
6. go inside project (main/setting.py) inside settings.py update in  { INSTALLED_APPS = ['rest_framework'] }
7. python manage.py migrate         // initial migrate command for migrating default models like admin and etc...
8. python manage.py runserver       // for running the server
=== Creating Super user ============================================================================================================
9. python manage.py createsuperuser // creating the super user({admin,root}) for login in admin pannel
10. python manage.py runserver goto {http://127.0.0.1:8000/admin/} //run the server again and try to login as {admin,root}
=== Creating New App ===============================================================================================================
11. python manage.py startapp home  // creating app (home)
12. go inside project (main/setting.py) inside settings.py update in  { INSTALLED_APPS = ['home'] }
==== Creating Models ===============================================================================================================
13. creating models inside (home/models.py) create a class and define the fields
14. go inside (home/admin.py) and register the model 
15. python manage.py makemigrations  // now make the migration for model
16. python manage.py migrate  // now migrate the updates of model 
=== setup serializer and APIViews ==================================================================================================
17. create a file of (serializer.py) and setup serializer
18. go to (home/views.py) create api using APIViews 
=== creating url ===================================================================================================================
19. goto (main/usls.py) and create a path for {home/} url
