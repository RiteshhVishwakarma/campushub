"""
Settings package for CampusHub.
Automatically imports the appropriate settings based on DJANGO_SETTINGS_MODULE.
"""
import os

# Default to development settings if not specified
environment = os.environ.get('DJANGO_ENV', 'development')

if environment == 'production':
    from .production import *
else:
    from .development import *
