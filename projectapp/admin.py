from django.contrib import admin  # Import the admin module from Django's built-in admin application
from .models import BlogPost  # Import the BlogPost model from the models.py file in the current directory

admin.site.register(BlogPost)  # Register the BlogPost model with Django's admin site
