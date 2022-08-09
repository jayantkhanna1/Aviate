from django.shortcuts import render,redirect
from .models import Categories, Jobs, JobApplication
from django.core.files.storage import FileSystemStorage
import string
import random

def index(request):
    return render(request,'index.html',{'jobs':Jobs.objects.all()})

def employeedashboard(request):
    return render(request,'employeedashboard.html',{'categories':Categories.objects.all()})

def createnewjob(request):
    jobname = request.POST['jobname']
    description = request.POST['description']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    startdate = request.POST['startdate']
    enddate = request.POST['enddate']
    category = request.POST['category']
    jobtype = request.POST['job_type']
    salary = request.POST['salary']
    gender = request.POST['gender']
    qualification = request.POST['qualification']
    experience = request.POST['experience']
    Jobs.objects.create(jobname = jobname, description = description, city = city, state = state, country = country, fromdate = startdate, todate = enddate, category = category, job_type = jobtype,gender= gender, qualification=qualification, experience=experience, salary=salary)
    return redirect('employeedashboard')

def oldjobs(request):
    return render(request,'jobs.html',{'jobs':Jobs.objects.all(),'category':Categories.objects.all()})


def opensinglejob(request):
    idd = request.GET['id']
    return render(request,'opensinglejob.html',{'job':Jobs.objects.get(id = idd)})

def searchjobs(request):
    id = request.GET['jobname']
    if id == "all":
        return render(request,'jobs.html',{'jobs':Jobs.objects.all(),'category':Categories.objects.all()}) 
    else:
        return render(request,'jobs.html',{'jobs':Jobs.objects.all(),'category':Categories.objects.all()})

def applyforjob(request):
    jobid = request.GET['jobid']
    return render(request,'applyforjob.html',{'job':Jobs.objects.get(id = jobid)})

def createnewapplication(request):
    jobname = request.POST['jobname']
    jobid = request.POST['jobid']
    name_of_applicant = request.POST['applicant_name']
    email = request.POST['applicant_email']
    phone = request.POST['applicant_mobile']
    resume =request.FILES['resume']
    cover_letter = request.POST['coverletter']
    applicant_city = request.POST['applicant_city']
    applicant_state = request.POST['applicant_state']
    applicant_country = request.POST['country']
    candidate_image = request.FILES['applicant_image']
    skills = request.POST['skills']
    gender = request.POST['gender']
    applicant_experience = request.POST['experience']
    candidate_qual = request.POST['qualification']
    dob = request.POST['dob']
    random_resume_name = ''.join(random.sample(string.ascii_letters+string.digits,12))
    random_resume_name = random_resume_name + '.pdf'
    random_img_name = ''.join(random.sample(string.ascii_letters+string.digits,12))
    random_img_name = random_img_name + '.jpg'
    FileSystemStorage().save("aviate_app/static/resume_applicants/"+random_resume_name, resume)
    FileSystemStorage().save("aviate_app/static/applicants_images/"+random_img_name, candidate_image)
    JobApplication.objects.create(jobname = jobname, jobid = jobid, name_of_applicant = name_of_applicant, email = email, phone = phone, resume = "static/resume_applicants/"+random_resume_name, cover_letter = cover_letter, applicant_city = applicant_city, applicant_state = applicant_state, applicant_country = applicant_country, candidate_image = "static/applicants_images/"+random_img_name, skills = skills,gender = gender, candidate_qual = candidate_qual, applicant_experience = applicant_experience, dob = dob)
    return redirect('index')
    
def candidates(request):
    return render(request,'candidates.html',{'candidates':JobApplication.objects.all()})

def opensinglecandidate(request):
    candidateid = request.GET['candidateid']
    candidate = JobApplication.objects.get(id = candidateid)
    job = Jobs.objects.get(id = candidate.jobid)
    return render(request,'opensinglecandidate.html',{'candidate':candidate,'job':job})