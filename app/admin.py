from django.contrib import admin
from .models import Student

class studentDetails(admin.ModelAdmin):
    list_display=('id','name','email','password','gender')
# Register your models here.
admin.site.register(Student,studentDetails)