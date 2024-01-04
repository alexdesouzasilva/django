from .settings import *

DEBUG = True

#Cria secret key para o ambiente de desenvolvimento

SECRET_KEY = 'alxDS0104'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}