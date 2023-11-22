import django.forms

from .models import UploadedFile
from django import forms

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['input_file']