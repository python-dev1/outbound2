from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('register2',views.registration2,name='register'),
    path('login_check',views.login_check,name='check'),
    path('get_report',views.getReport,name='report'),
    path('single',views.single,name='sngl'),
    path('cfile',views.cfile,name='cfle'),
    path('file_scores',views.file_score,name='cfscore'),
    # path('get_report',views.getReport,name='report'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)