# from django.contrib import admin

# from django.contrib.admin import ModelAdmin, register


# from .models import Person

# @register(Person)
# class PersonAdmin(ModelAdmin):
#     list_display = ('first_name', 'last_name','age')
#     icon_name='accessibility'

from django.contrib import admin
from .models import Task,Emp

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['task','user','emp','select']
    icon_name='add_task'

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display=['name']
    icon_name='person'
    