from django.contrib import admin
from .models .user import User
from .models.user import Post


# Register your models here.
admin.site.register(User)
admin.site.register(Post)