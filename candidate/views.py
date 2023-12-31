from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from hr.models import JobPost , CandidateApplications
from candidate.models import MyApplyJobList
from django.contrib import messages
from .forms import ProfileForm

# Create your views here.

@login_required
def candidateHome(request):
    jobpost = JobPost.objects.all()
    return render(request,'candidate/dashboradh.html',{'jobpost':jobpost})

@login_required
def applyJob(request, id):
    job = get_object_or_404(JobPost, id=id)
 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        college = request.POST.get('college')
        passing_year = request.POST.get('passing_year')
        yearOfExperience = request.POST.get('yearOfExperience')
        resume = request.FILES.get('resume')

        # Check if the user has already applied to this job
        if CandidateApplications.objects.filter(user=request.user, job=job).exists():
            messages.warning(request, 'You have already applied to this job.')
            return redirect('dash')

        # Create a new application
        application = CandidateApplications(
            user=request.user,
            job=job,
            passingYear=passing_year,
            yearOfExperience=yearOfExperience,
        )

        # Check if resume file is provided before saving
        if resume:
            application.resume = resume
            application.save()
            messages.success(request, 'Application submitted successfully.')
            return redirect('dash')
        else:
            messages.error(request, 'Please provide a resume file.')
    else:
        return render(request, 'candidate/apply.html')


@login_required
def myjoblist(request):
    joblist = MyApplyJobList.objects.filter(user=request.user)
    return render(request,'candidate/myjoblist.html',{'joblist':joblist})

def profilepage(request):
    context = {
        'user': request.user
    }
    return render(request, 'candidate/profile.html', context)

def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page after successful editing
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'candidate/edit_profile.html', {'form': form})


def candidate_applications(request):
    user_applications = CandidateApplications.objects.filter(user=request.user)
    return render(request, 'candidate/candidate_applications.html', {'applications': user_applications})

