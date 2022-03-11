from django.contrib import admin

# Register your models here.

from .models import Ibovespa, Dollar

admin.site.register(Ibovespa)
admin.site.register(Dollar)