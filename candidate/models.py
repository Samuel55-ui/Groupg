from django.db import models
from hr.models import JobPost , CandidateApplications
from django.contrib.auth.models import User
# Create your models here.


class MyApplyJobList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_application = models.ForeignKey(CandidateApplications, on_delete=models.CASCADE)
    dateYouApply = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job_application')

class IsSortList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    dateYouApply = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    qualifications = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} profile'