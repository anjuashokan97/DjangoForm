from django.contrib import admin
from .models import Resume


# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'gender', 'locality', 'city', 'pin_code', 'state', 'mobile', 'email', 'courses')


admin.site.register(Resume, ResumeAdmin)
