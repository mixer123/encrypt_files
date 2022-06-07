import mimetypes
from os.path import join

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from cryptography.fernet import Fernet
import  base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required

# Create your views here.
import os
from . import encrypt_lib

from encrypt.encrypt_lib import *
from .models import *
from .forms import UploadForm



''' Upload file '''
def listusers(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def upload(request):
        user = User.objects.get(username=patern)
        # dir = 'media/'
        #
        # for f in os.listdir(dir):
        #     if os.path.isfile(dir):
        #       os.remove(os.path.join(dir, f))

        if request.method == 'POST':
                form = UploadForm(request.POST, request.FILES)
                if form.is_valid():
                    file = Upload(file=request.FILES['file'], user_id=user.id)
                    file.save()
                    file_patern = request.FILES['file']
                    file = FileEncrypt(str(file_patern), 'salt.txt', 'media', 'media/salt')
                    password = b'Mirek123!'
                    file.encrypt_file()
                    return redirect('/')
        else:
                    form = UploadForm()  # A empty, unbound form
        return render(request, 'upload.html', {'form':form})



#
# def uploadfile(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         file = FileEncrypt(filename, 'salt.txt', 'media', 'media/salt')
#         password = b'Mirek123!'
#
#         file.encrypt_file()
#
#         return render(request, 'uploadfile.html', {'uploaded_file_url': uploaded_file_url })
#     return render(request, 'uploadfile.html')
# def show_files(request):
#     path = 'media'
#     listdir = [f for f in os.listdir(path) if f[-3:] == 'txt']
#     return render(request, 'listdir.html', {'listdir':listdir})
@login_required(login_url='/accounts/login/')
def download_list(request):

    # files = Upload.objects.all()
    files = Upload.objects.all().prefetch_related('user')
    # files = Upload.objects.all().select_related('user')
    # files = Upload.objects.filter(user__username='ORYGINAL').values('file', 'username')
    return render(request, 'download_list.html', {'files': files, 'user': request.user.username})


def download_file(request,file_name):
    # Define Django project base directory
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = file_name
    file = FileDecrypt(filename,'salt.txt','media','media/salt')
    file.decrypt_file()
    # Define the full file path
    filepath = 'media/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    os.remove(filepath) # usuwanie pliku pobranego
    # Return the response value
    return response

def success(request):
    return render(request, 'success.html')
def start(request):
    return render(request, 'start.html')


def uploadfile(request):
    patern = request.GET['nameuser']
    print('patern',type(patern), patern)
    user = User.objects.get(username=patern)
    print('user',user, type(user), user.id)
    obj = get_object_or_404(User, id=user.id)
    try:
        # Handle file upload
        if request.method == 'POST':
            form = UploadForm1(request.POST, request.FILES)
            if form.is_valid():
                file = Upload(file=request.FILES['file'], user_id=user.id)
                file.save()
                return redirect('/')
        else:
            form = UploadForm1() # A empty, unbound form
    except IndexError:
        return redirect('/')




    # Render list page with the documents and the form
    return render(request, 'uploadfile.html', {'form': form})