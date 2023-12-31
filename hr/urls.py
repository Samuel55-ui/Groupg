from django.urls import path
from hr import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CandidateProfileView

urlpatterns = [
    path('hrdash/',views.hrHome,name='hrdash'),
    path('candidatedetails/<int:id>/',views.hrCandidateDetails,name='candidatedetails'),
    path('postjob/',views.postJobs,name='postjob'),
    path('acceptapplication/',views.acceptApplication,name='acceptapplication'),
    path('profilehr/',views.profilepagehr,name='profilehr'),
    path('reject_application/', views.reject_application, name='rejectapplication'),
    path('candidate_profile/<int:user_id>/', views.candidate_profile, name='candidate_profile'),
    path('edit-profilehr/', views.edit_profilehr, name='edit_profilehr'),
     
]

if settings.DEBUG:  
     urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
