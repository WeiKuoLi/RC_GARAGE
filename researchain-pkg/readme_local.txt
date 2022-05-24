LOCAL SETUP INSTRUCTION
2022.5.3

push & pull from github sucess!
use ssh for git push/pull

once download,  use anaconda tensorflow virtual env to probe the files

multiple packages are needed. 
$pip install -r requirement.txt
some additional django-apps are required.

see AA/setting.py to see INSTALLED_APPS ex. pip install django-allauth
requirements.txt are manually tweaked for future convenience

* psycopg2 & psycopg2-binary cannot be download before postgreSQL
becuase pg_config cannot be found in system $PATH  (suggested from error
messages =D)

install postgreSQL from home page of postgreSQL, use EDB to install.
after installation find the position of the installed files.
find C:\....\postgreSQL\12\bin : file pg_config is under this bin

add this path to $PATH in settings->about this pc-> advansed system
settings->environment variables ->system variables->path->edit->new -> _______

*btw download mingw & gvim. they are important and handy.  also there paths should be added to $PATH by method
mentioned above

pip install psycopg2 & psycopg2-binary  succesfully.
 
pip install django-cors-headers 

set up database ! use pgAdmin. VERY HANDY
login with postgres superuser 

fill in these info. to AA/settings : DATABASES = ...
PORT is '5432' try '5433' if failed

add "https://" before all CSRF_TRUSTED_ORIGINS paths or else new version
django cannot work

python manage.py migrate
python manage.py runserver

*** remember to setup allauth third party registration, local database info under AA/settings.py


useful resource:
******https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github
******https://aben20807.blogspot.com/2018/03/1070302-git-push-ssh-key.html
******https://github.com/settings/keys
1. origin can be other names ex github, weikuo if origin already exists

*******https://docs.djangoproject.com/en/4.0/intro/tutorial02/
1.Change your models (in models.py).
2.python manage.py makemigrations        |to create migrations for those changes
3.python manage.py migrate              |to apply those changes to the database.








2022.05.03

journals app are changed 
views.py are created & backed up as views-old.py

accounts\urls.py are changed at line 9
accounts\views.py are change at line 79,80 
"..\templates\account\signup.html" are changed at line 146
"..\templates\account\weikuo.html" are created for login from github
AA:settings.py are changed at line 63 85 260 261

note email verification is turned off!






