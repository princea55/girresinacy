from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(User):
    USERNAME_FIELD = 'email'
    contact = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "User"

class ContactUs(models.Model):
    fullName = models.CharField(max_length=20)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fullName
    
    class Meta:
        verbose_name_plural = "ContactUs"