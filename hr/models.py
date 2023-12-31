from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Hr(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)


class JobPost(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    compnayName = models.CharField(max_length=100)
    role = models.CharField(max_length=100,default='anything')
    salaryLow = models.IntegerField(default=0)
    salaryHigh = models.IntegerField(default=0)
    applyCount =  models.IntegerField(default=0)
    lastDateToApply = models.DateField()

    def __str__(self):
        return str(self.title)


STATUS_CHOICE = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)

class CandidateApplications(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    job = models.ForeignKey(to=JobPost,on_delete=models.CASCADE)
    passingYear = models.IntegerField()
    yearOfExperience = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume', null=True)
    status = models.CharField(choices=STATUS_CHOICE,max_length=20,default='pending')

    def __str__(self):
        return str(self.user.username)+" "+str(self.job.title)


class SelectCandidateJob(models.Model):
    job = models.ForeignKey(to=JobPost,on_delete=models.CASCADE)
    candidate = models.OneToOneField(to=CandidateApplications,on_delete=models.CASCADE)

class Profilehr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    qualifications = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} profile'