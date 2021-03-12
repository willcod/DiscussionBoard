from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = "users"

urlpatterns = [
    # path('', include('django.contrib.auth.urls'))
    url(r'^login/$', LoginView.as_view(template_name= 'users/login.html'),
        name='login'),
        
    # Logout page.
    url(r'^logout/$', views.logout_view, name='logout'),
]
