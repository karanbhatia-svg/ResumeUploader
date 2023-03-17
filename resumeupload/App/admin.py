from django.contrib import admin

from .models import resume

@admin.register(resume)
class ResumeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']