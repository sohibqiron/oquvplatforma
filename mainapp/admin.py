from django.contrib import admin
from .models import Mentor,Student,UserProfile,Group
# Register your models here.

admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(UserProfile)
admin.site.register(Group)