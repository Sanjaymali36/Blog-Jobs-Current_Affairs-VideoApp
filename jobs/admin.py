from django.contrib import admin

# Register your models here.

from django.contrib import admin

from tinymce.widgets import TinyMCE
from django.db import models

from .models import *


class JobsAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["job_title", "job_department","notification","qualification","last_date", "apply_link"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }













class DepartmentWiseJobsAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["jobs_details","title","topic","created_by","link1","link2","link3"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class LoctionWiseJobsAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["job_details","title","topic","created_by","link1","link2","link3"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
admin.site.register(Location)
admin.site.register(Location_Category)
admin.site.register(LoctionWiseJobs,LoctionWiseJobsAdmin)

admin.site.register(Departments)
admin.site.register(Department_sub_Category)
admin.site.register(DepartmentWiseJobs,DepartmentWiseJobsAdmin)
admin.site.register(Jobs,JobsAdmin)

