from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('new_article/', views.new_article, name='new_article'),
]