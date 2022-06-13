from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    re_path('^$',views.home,name='home'),
    # re_path('accounts/register/', views.register, name='register'),
    re_path(r'^search/',views.search_results,name='search_results'),
    re_path('new_project/', views.new_project,name ='new_project'),
    re_path('ratings/<post>/', views.project, name='ratings'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)