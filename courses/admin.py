from django.contrib import admin
from .models import Lesson, Course, Comment, Rate

# Register your models here.


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('comment', 'created_at', 'lesson', 'user')
    search_fields = ('user', 'lesson', 'comment')
    readonly_fields = ('created_at',)


@admin.register(Rate)
class UserAdmin(admin.ModelAdmin):
    list_display = ('rate', 'created_at', 'lesson', 'user')
    search_fields = ('user', 'lesson', 'rate')
    readonly_fields = ('created_at',)
