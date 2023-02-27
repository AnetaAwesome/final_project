from django.contrib import admin
from .models import BlogPost, Contact, Comment

admin.site.register(BlogPost)
admin.site.register(Contact)
admin.site.register(Comment)
