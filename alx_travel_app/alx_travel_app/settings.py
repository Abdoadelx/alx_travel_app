# settings.py

"""
Django settings for your_project_name project.

This file contains the core configuration for your Django project.
It's like the central control panel where you define how different
parts of your application behave.
"""

# Import necessary libraries.
# - pathlib: For handling file system paths in a modern, object-oriented way.
# - os: Provides a way of using operating system dependent functionality.
# - environ (optional but recommended): For loading environment variables from a .env file.
import os
from pathlib import Path
import environ

# --- Core Paths ---
# This section defines the fundamental directory paths for the project.

# BASE_DIR points to the root of your project folder.
# It's used to build all other paths, ensuring your project is portable.
# Example: /home/user/my_django_project/
BASE_DIR = Path(__file__).resolve().parent.parent


# --- Environment Variable Setup (Optional but Recommended) ---
# This setup allows you to keep sensitive information (like passwords and API keys)
# out of your code by storing them in a separate `.env` file.

# Initialize the environ library.
env = environ.Env(
    # Set default values and data types for environment variables.
    # This prevents the app from crashing if a variable isn't set.
    DEBUG=(bool, False) # Defaults DEBUG to False if not found in .env
)

# Specify the path to your .env file and read it.
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# --- Security Settings ---
# These settings are crucial for protecting your application from common vulnerabilities.

# SECRET_KEY: A long, random string used for cryptographic signing (e.g., sessions).
# Keep this secret! It's loaded from the .env file for security.
SECRET_KEY = env('SECRET_KEY')

# DEBUG: A boolean that toggles debug mode.
# When True, Django shows detailed error pages.
# NEVER run a production server with DEBUG = True. This is also loaded from .env.
DEBUG = env('DEBUG')

# ALLOWED_HOSTS: A list of strings representing the host/domain names
# that this Django site can serve. It's a security measure to prevent
# HTTP Host header attacks. For development, it's often empty or ['*'].
# For production, you must list your domain(s), e.g., ['www.example.com'].
ALLOWED_HOSTS = []


# --- Application Definitions ---
# This is where you register all the "apps" that make up your project.

# INSTALLED_APPS tells Django which applications are active for this site.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party Apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',  # <-- Add this line

    # Local Apps
    'listings',
]


# --- Middleware Configuration ---
# Middleware is a framework of hooks into Django's request/response processing.
# Think of it as layers of security and functionality that every request passes through.
# The order is important!

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # Adds several security enhancements.
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages user sessions.
    # 'corsheaders.middleware.CorsMiddleware',               # Handles CORS headers (place high).
    'django.middleware.common.CommonMiddleware',             # Handles basic URL processing.
    'django.middleware.csrf.CsrfViewMiddleware',             # Adds Cross-Site Request Forgery protection.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',    # Enables cookie- and session-based messaging.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protects against clickjacking.
]


# --- URL Configuration ---
# This setting points to the file where your project's main URL patterns are defined.

ROOT_URLCONF = 'alx_travel_app.urls' # Replace 'your_project_name'


# --- Template Configuration ---
# This section defines how Django finds and renders HTML templates.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # A list of directories where Django should look for templates.
        'APP_DIRS': True, # Tells Django to look for templates inside each app's 'templates' folder.
        'OPTIONS': {
            'context_processors': [ # These make variables globally available in all templates.
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# --- WSGI Application ---
# This setting points to the WSGI application object that Django's built-in
# development server (and production servers) will use.

WSGI_APPLICATION = 'alx_travel_app.wsgi.application' # Replace 'your_project_name'


# --- Database Configuration ---
# Here you define the connection settings for your project's database(s).
# The settings are loaded from the .env file for security.

DATABASES = {
    'default': env.db(), # This smart function from django-environ reads DATABASE_URL from .env
                         # Example .env line: DATABASE_URL=mysql://user:password@host:port/dbname
    
    # Alternative, manual configuration if you don't use DATABASE_URL:
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': env('DATABASE_NAME'),
    #     'USER': env('DATABASE_USER'),
    #     'PASSWORD': env('DATABASE_PASSWORD'),
    #     'HOST': env('DATABASE_HOST'),
    #     'PORT': env('DATABASE_PORT'),
    # }
}


# --- Password Validation ---
# This section lists validators that are used to check the strength of users' passwords.

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# --- Internationalization (i18n) and Localization (l10n) ---
# These settings configure language and time zone support for your application.

LANGUAGE_CODE = 'en-us' # The default language for the site.

TIME_ZONE = 'Africa/Cairo' # The default time zone.

USE_I18N = True # Enable Django's translation system.

USE_TZ = True # Enable timezone-aware datetimes.


# --- Static Files (CSS, JavaScript, Images) ---
# This section defines how Django handles static files during development and deployment.

STATIC_URL = 'static/' # The URL prefix for static files. e.g., /static/css/style.css

# A list of directories where Django will look for static files, in addition
# to each app's 'static' folder.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# The absolute path to the directory where `collectstatic` will collect static files
# for deployment. This should be different from STATICFILES_DIRS.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# --- Media Files (User-Uploaded Content) ---
# This section defines how Django handles files uploaded by users.

MEDIA_URL = '/media/' # The URL prefix for media files.

# The absolute path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# --- Default Primary Key Field Type ---
# This sets the default type of primary key to use for models that don't
# explicitly define one. BigAutoField is a 64-bit integer.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'