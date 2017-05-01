from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),

    url(r'^login/$', views.UserLoginFormView.as_view(), name='login'),

    url(r'^register/$', views.UserRegistrationFormView.as_view(), name='register'),

    url(r'^logout/$', views.logOut, name='logout')
]