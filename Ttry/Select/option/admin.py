from django.contrib import admin

from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Category']
admin.site.register(Category, CategoryAdmin)



class CourseAdmin(admin.ModelAdmin):
    list_display = ['Course_Name', 'category']
admin.site.register(Course, CourseAdmin)