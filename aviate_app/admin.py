from django.contrib import admin
from .models import Categories, Jobs, JobApplication
# Register your models here.
admin.site.register(Categories)
admin.site.register(Jobs)
admin.site.register(JobApplication)