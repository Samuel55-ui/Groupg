from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from hr.models import JobPost , CandidateApplications , SelectCandidateJob
from candidate.models import IsSortList
from .forms import ProfileForm
# Create your views here.

@login_required
def hrHome(request):
    jobposts = JobPost.objects.filter(user=request.user)

    print(jobposts)
    return render(request,'hr/hrdashbordh.html',{'jobposts':jobposts})

@login_required
def hrCandidateDetails(request,id):
    if JobPost.objects.filter(id=id).exists():
        jobpost = JobPost.objects.get(id=id)
        jobapplys = CandidateApplications.objects.filter(job=jobpost)
        # print(jobapplys)
        selectedCandidate = SelectCandidateJob.objects.filter(job=jobpost)
        print(selectedCandidate)
        return render(request,'hr/candidate.html',{'jobapplys':jobapplys,'jobpost':jobpost,'selectedCandidate':selectedCandidate})
    else:
        return render('hrdash') 

@login_required
def postJobs(request):
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        role=request.POST.get('role')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date  = request.POST.get('last-date')

        jobpost = JobPost(user=request.user,title=job_title,address=address,compnayName=company_name,role=role,salaryLow=salary_low,salaryHigh=salary_high,lastDateToApply=last_date)
        jobpost.save()
        msg = "Job Upload Done.."
        return render(request,'hr/postjob.html',{'msg':msg})
    return render(request,'hr/postjob.html')

def acceptApplication(request):
    if request.method == 'POST':
        candidateid = request.POST.get('candidateid')
        jobpostid = request.POST.get('jobpostid') 

        # Retrieve the candidate application
        candidate = CandidateApplications.objects.get(id=candidateid) 

        # Update the status to 'accepted'
        candidate.status = 'accepted'
        candidate.save()

        # Create SelectCandidateJob and IsSortList records
        if not SelectCandidateJob.objects.filter(candidate=candidate).exists():
            jobpost = JobPost.objects.get(id=jobpostid)
            SelectCandidateJob.objects.create(job=jobpost, candidate=candidate)
            IsSortList.objects.create(user=candidate.user, job=jobpost)

        return redirect('/candidatedetails/' + str(jobpostid) + '/')
    
    return redirect('hrdash')


def reject_application(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('candidateid')
        job_post_id = request.POST.get('jobpostid')

        # Ensure that candidate_id and job_post_id are not None
        if candidate_id is not None and job_post_id is not None:
            try:
                candidate_id = int(candidate_id)
                job_post_id = int(job_post_id)
            except ValueError:
                # Handle invalid input
                messages.error(request, 'Invalid input for candidate or job post ID.')
                return redirect('hrdash')  # Replace 'hrdash' with the appropriate URL

            # Retrieve the candidate application
            candidate_application = get_object_or_404(CandidateApplications, id=candidate_id, job_id=job_post_id)

            # Update the status to 'rejected'
            candidate_application.status = 'rejected'
            candidate_application.save()

            # Delete the candidate application
            candidate_application.delete()

            messages.success(request, 'Application rejected successfully.')
            return redirect('hrdash')  # Replace 'hrdash' with the appropriate URL

        else:
            # Handle cases where candidate_id or job_post_id is None
            messages.error(request, 'Candidate or job post ID is missing.')
            return redirect('hrdash')  # Replace 'hrdash' with the appropriate URL

    # Handle cases where the view is accessed directly without a POST request
    messages.error(request, 'Invalid request method.')
    return redirect('hrdash')  # Replace 'hrdash' with the appropriate URL

from django.shortcuts import render


class CandidateProfileView(View):
    template_name = 'candidate/profile.html'

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        # Add any additional logic to retrieve candidate profile data
        return render(request, self.template_name, {'user': user})
    

def candidate_profile(request, user_id):
    candidate_user = get_object_or_404(User, id=user_id)
    return render(request, 'hr/candidate_profile.html', {'candidate_user': candidate_user})


def profilepagehr(request):
    context = {
        'user': request.user
    }
    return render(request, 'hr/profilehr.html', context)


def edit_profilehr(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profilehr')  # Redirect to the user's profile page after successful editing
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'hr/edit_profilehr.html', {'form': form})