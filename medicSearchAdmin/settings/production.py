from .settings import *

DEBUG = False

#Cria secret key do ambiente de produção
SECRET_KEY = 'ALX5#%4$'

DATABASES = {
    'defaul': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}