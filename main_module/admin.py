from django.contrib import admin

# Register your models here.

from .models import registration,login,files


admin.site.register(registration)
admin.site.register(login)
admin.site.register(files)