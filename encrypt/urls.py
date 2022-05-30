from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

from . import views
from .forms import UploadForm

urlpatterns = [

    path('upload/', views.uploadfile, name="uploadfile-page"),
    path('listdir/', views.show_files, name="listdir-page"),
    path('download/<str:file_name>/', views.download_file, name="download-page"),

    ]