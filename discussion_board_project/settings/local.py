from .base import *

print('local settings applied')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+r8l_vu^k(i*upia)r$rclaul2$59we6l7f=v#p-f90rod92@z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]