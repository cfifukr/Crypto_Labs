from django.db import models

class UploadedFile(models.Model):
    input_file = models.FileField(upload_to='uploads/')
    output_file = models.FileField(upload_to='uploads/')
