from os.path import join

from django.core.files.storage import FileSystemStorage
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
        myfile1 = request.FILES.get('myfile', None)
        print('myfile1', myfile1)

        file = encrypt_lib.FileEncrypt(myfile1.name)

        file.encrypt_file()
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        return render(request, 'uploadfile.html', {'uploaded_file_url': uploaded_file_url })
    return render(request, 'uploadfile.html')
def show_files(request):
    path = 'media'
    path_salt = 'media/salt'
    listdir = [f for f in os.listdir(path) if f[-3:] == 'txt']
    file_from_list = listdir[0]
    file = FileEncrypt(file_from_list,'salt.txt','media','media/salt')
    password = b'Mirek123!'
    text = file.read()
    file.encrypt_file()
    return render(request, 'listdir.html', {'listdir':listdir, 'file':file})

def inside_file(request):
    path = 'media'
    listdir = [f for f in os.listdir(path) if f[-3:] == 'txt']
    file = listdir[0]
    with open(os.path.join(path, file), 'r') as f:
        text = f.read()
    return render(request, 'inside_file.html', {'text':text})

#
# def encrypt_file(request):
#     file = encrypt_lib.FileEncrypt('plik_do_pracy_domowej.txt', 'salt.txt')