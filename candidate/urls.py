from django.urls import path
from candidate import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('dash/',views.candidateHome,name='dash'),
     path('applyjob/<int:id>/',views.applyJob,name='apply'),
     path('applylist/',views.myjoblist,name='mylist'),
     path('profile/',views.profilepage,name='profile'),
     path('edit-profile/', views.edit_profile, name='edit_profile'),
     path('candidate_applications/', views.candidate_applications, name='candidate_applications'),
]


if settings.DEBUG:  
     urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)