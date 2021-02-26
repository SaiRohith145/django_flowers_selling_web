from django.contrib import admin
from .models import flower_type,comment_db
# Register your models here.
admin.site.register(flower_type)
admin.site.register(comment_db)