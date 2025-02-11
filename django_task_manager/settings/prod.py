from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
load_dotenv()
DEBUG = os.getenv("DJANGO_DEBUG", "False") != "False"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "task-manager-qo2g.onrender.com"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.environ.get('POSTGRES_DB'),
           'USER': os.environ.get('POSTGRES_USER'),
           'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
           'HOST': os.environ.get('POSTGRES_HOST'),
           'PORT': '5432',
       }
   }
