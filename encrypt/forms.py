from django import forms
from django.core.validators import FileExtensionValidator
from .models import *
# class UploadForm(forms.Form):
#
#     file = forms.FileField(
#         label='Dołącz plik txt',
#         help_text='max. 1MB',
#         validators=[FileExtensionValidator(allowed_extensions=['txt'])])
#     user = forms.CharField()

class UploadForm(forms.Form):

    file = forms.FileField(
        label='Dołącz plik txt',
        help_text='max. 1MB',
        validators=[FileExtensionValidator(allowed_extensions=['txt'])])
