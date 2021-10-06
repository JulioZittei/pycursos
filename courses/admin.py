from django.contrib import admin
from .models import Classes, Courses

# Register your models here.


@admin.register(Courses)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Classes)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
