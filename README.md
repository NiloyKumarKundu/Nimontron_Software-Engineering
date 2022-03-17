# Food-Delivery-App---Django

To create virtual env use the command - 

- Windows:
```
py -m virtualenv venv
```
- Mac:
```
python3 -m virtualenv venv
```

To check venv is created or not
```
Windows: dir
Mac: ls
```

To activate virtual env use command
- Windows:
```
venv\scripts\activate
```
- Mac:
```
source venv/bin/activate
```

To install django
- windows:
```
pip install django
```
- mac:  
```
pip3 install django
```

To check the django version, use command - 
- windows:
```
py -m django --version
```
- mac:  
```
python3 -m django --version
```

To create a django project
- windows:
```
py -m django startproject Nimontron
```
- mac:  
```
python3 -m django startproject Nimontron
```


Urls.py -> We will use it to create links to the views of our app.
Settings.py -> It is the file for the configuration of the project.



For migration -
- windows:
```
py manage.py makemigrations
py manage.py migrate
```
- mac: 
```
python3 manage.py makemigrations
python3 manage.py migrate
```

For run the server - 
- windows:
```
py manage.py runserver
```
- mac: 
```
python3 manage.py runserver
```


For adding the admin control in django -
- windows:
```
py manage.py createsuperuser
```
- mac: 
```
python3 manage.py createsuperuser
```

If you want to add a models/class in admin/database
You need to register this model in admin page -
Go to admin page in the app
```
admin.site.register(Model_name)
```



# Work with git & github

For working this repository, at first you need to clone this repo on your local machine.
For this try this command, 
```
git clone https://github.com/NiloyKumarKundu/Food-Delivery-App---Django
```

After clone this repository, Now make sure that your git global email is set.
If not run this command.
```
git config --global user.email "YOUR_EMAIL_HERE"
```
Replace YOUR_EMAIL_HERE with **your mail address** which is your github login email.


After doing some changes, you can now add your file in this repository.
If you want to see the modification files, run this command in your CMD/Terminal.
```
git status
```

For adding this changes, you need to enter this command.
```
git add .
```

Now commit this adding files with a message
```
git commit -m "Nimontron"
```

Now push this files into this repository. For that run this command.
```
git push
```

Hurrrah!! You complete all steps. Now go to the original git folder with your brower and you can see the changes there!
Thank you!