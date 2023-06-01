# Wiki-aryia-backend
 To run a Django project follow these steps:

1.Download the Project from GitHub

2.Create Virtual Environment you project repository
` python -m venv myenv`

3.Activate your virtual Env:
` myenv\Scripts\activate`

4.Install all the requirement packages:
` pip install -r requirements.txt`

5.connect your databases in /wikiariya/settings.py
` INSTALLED_APPS = [
'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wikiariya',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
]
`

6.Migrate all the models:
` python manage.py migrate`

7.Run the project
` python manage.py runserver`



