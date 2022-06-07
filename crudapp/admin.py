from django.contrib import admin
from .models import name,age,gender

# Register your models here.
admin.site.register(name)
admin.site.register(age)
admin.site.register(gender)