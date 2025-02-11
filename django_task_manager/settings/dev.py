from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
load_dotenv()
DEBUG = True

ALLOWED_HOSTS = ["task-manager-qo2g.onrender.com"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
