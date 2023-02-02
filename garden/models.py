from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    subject=models.TextField()
    msg=models.TextField()
