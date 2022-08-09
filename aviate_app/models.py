from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)

class Jobs(models.Model):
    jobname = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    city = models.CharField(max_length=100)
    salary = models.IntegerField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    fromdate = models.CharField(max_length=100)
    todate = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Active")

class JobApplication(models.Model):
    jobname = models.CharField(max_length=100)
    jobid = models.CharField(max_length=100)
    name_of_applicant = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    cover_letter = models.CharField(max_length=100)
    applicant_city = models.CharField(max_length=100)
    applicant_state = models.CharField(max_length=100)
    applicant_country = models.CharField(max_length=100)
    candidate_image = models.CharField(max_length=100)
    applicant_experience = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    candidate_qual = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)