from django.conf.urls.static import static 
from django.conf import settings 
from django.urls import path 

from .views import contact_view, create_cv, cv_list, share_cv_email


urlpatterns = [ 
    path('contact/', contact_view, name='contact'), 
    path('cv/', create_cv),
    path('cv-list/', cv_list, name='cv_list'),
    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 