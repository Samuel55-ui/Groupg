from django.contrib import admin
from candidate import models
from .models import Profile
# Register your models here.


@admin.register(models.MyApplyJobList)
class MyApplyJobListAdmin(admin.ModelAdmin):
    list_display = ('id','user','job_application','dateYouApply')

@admin.register(models.IsSortList)
class IsSortListAdmin(admin.ModelAdmin):
    list_display = ('id','user','job','dateYouApply')

admin.site.register(Profile)
