from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.start, name="start-page"),
    path('upload/', views.upload, name="upload-page"),
    path('uploadfile/', views.uploadfile, name="uploadfile-page"),
    path('listusers/', views.listusers, name="listusers-page"),
    path('success/', views.success, name="success-page"),
    path('download/<str:file_name>/', views.download_file),
    path('download/', views.download_list, name='download-page'),
    ]