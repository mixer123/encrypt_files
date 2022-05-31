from django import forms
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    docfile = forms.FileField(
        label='Dołącz plik txt',
        help_text='max. 1MB',
        validators=[FileExtensionValidator(allowed_extensions=['txt' ])])