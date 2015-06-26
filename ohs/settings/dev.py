from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = os.getenv('SECRET', '58o2my)=@l88=mso-h*npjz!g)qqywv=v3yp-b*2!gzvvv%=k!')

# SQLite (simplest install)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

try:
    from .local import *
except ImportError:
    pass
