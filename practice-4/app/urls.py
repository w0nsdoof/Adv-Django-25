from django.conf.urls.static import static 
from django.conf import settings 
from django.urls import path 

from .views import contact_view, create_cv, cv_list


urlpatterns = [ 
    path('contact/', contact_view, name='contact'), 
    path('cv/', create_cv),
    path('cv-list/', cv_list, name='cv_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 