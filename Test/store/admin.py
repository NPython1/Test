from django.contrib import admin
from .models import Course, Department, Member
# Register your models here.


admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Member)

