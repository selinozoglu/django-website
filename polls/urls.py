from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('makale/<slug:slug>/', views.article, name='makale')
]

urlpatterns += staticfiles_urlpatterns()
