from .settings import *

DEBUG = True

#Cria secret key para o ambiente de testing
SECRET_KEY = 'AÇXLSLSL00%@'

DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}