from django.urls import include, re_path
from django.contrib import admin
urlpatterns = [
     re_path('notices/', include('notices.urls')), 
]
