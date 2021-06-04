from .base import *
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'local_db.sqlite3'),
        'USER': 'user_local'
    }
}
