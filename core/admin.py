
from django.contrib import admin
from .models import Department, Employee, Course, TrainingRecord


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_code',
        'first_name',
        'last_name',
        'email',
        'salary',
        'department',
        'is_active'
    )
    list_filter = ('department', 'is_active')
    search_fields = ('employee_code', 'first_name', 'last_name', 'email')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'capacity')
    search_fields = ('code', 'title')


@admin.register(TrainingRecord)
class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'course',
        'completion_status',
        'score',
        'enrollment_date'
    )
    list_filter = ('completion_status', 'course')
    search_fields = ('employee__employee_code', 'course__code')
