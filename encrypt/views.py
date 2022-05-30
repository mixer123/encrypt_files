import mimetypes
from os.path import join

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from cryptography.fernet import Fernet
import  base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.core.files.storage import default_storage

# Create your views here.
import os
from . import encrypt_lib

from encrypt.encrypt_lib import *

from encrypt.forms import UploadForm



''' Upload file '''
def uploadfile(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        file = FileEncrypt(filename, 'salt.txt', 'media', 'media/salt')
        password = b'Mirek123!'

        file.encrypt_file()

        return render(request, 'uploadfile.html', {'uploaded_file_url': uploaded_file_url })
    return render(request, 'uploadfile.html')
def show_files(request):
    path = 'media'
    listdir = [f for f in os.listdir(path) if f[-3:] == 'txt']
    return render(request, 'listdir.html', {'listdir':listdir})

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

