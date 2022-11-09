from .base import *  # noqa: F401,F403
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!hez$amw29bl$#%+85$rj!diz*8k6m9igvz%1=%lb7asvn3*to'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Overrides of base settings for local configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
        'ATOMIC_REQUESTS': True,
    }
}
