# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ebaxlfr&ksosgpf7=p23jiu5%x1lg7e$qg8v&@-mh!lta06spt'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
