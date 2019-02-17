from django.contrib import admin

from app.models import Post # наша модель из blog/models.py

admin.site.register(Post)