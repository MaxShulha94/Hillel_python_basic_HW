from django.contrib import admin
from .models import School, Student, Group

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    raw_id_fields = ('school',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    search_fields = ['name']
    raw_id_fields = ('group',)
