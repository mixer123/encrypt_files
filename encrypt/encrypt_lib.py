import os

from cryptography.fernet import Fernet
import  base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import walk, makedirs, rmdir
from os import listdir
from os.path import isfile, join

class Common:
    SALT = b'Python'
    PASSWORD = b'Mirek123!'
    def __init__(self, name_file, name_salt, path_file, path_salt):
        self.name_file = name_file
        self.name_salt = name_salt
        self.path_file = path_file
        self.path_salt = path_salt

    def read_salt(self):
        with open(os.path.join(self.path_salt,self.name_salt), 'r') as salt:
            salt1 = bytes(salt.read().encode('utf8'))
        return salt1

    def read(self):
        with open(os.path.join(self.path_file,self.name_file), 'r') as f:

            text = f.read()
        return text
    def read_bytes(self):
        with open(os.path.join(self.path_file,self.name_file), 'r') as file:
            text = file.read().encode('utf8')
            text=bytes(text)
        return text

    def create_key(self, password):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.read_salt(),
            iterations=390000
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def get_file(self):
        listdir = [f for f in os.listdir(self.path_file) if f[-3:] == 'txt']
        file_from_list = listdir[0]
        return file_from_list

class FileEncrypt(Common):
    def encrypt_file(self):
        fernet = Fernet(self.create_key(Common.PASSWORD))
        text = self.read()
        encrypt_text = fernet.encrypt(text.encode('utf8'))
        with open(os.path.join(self.path_file,self.name_file), 'w') as file:
            text= file.write(encrypt_text.decode('utf8'))
        return encrypt_text # funkcja zwraca zakodowany i zszyfrowany text w bytach

