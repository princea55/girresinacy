from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    contact=models.CharField(max_length=10)

class ContactUs(models.Model):
    fullName = models.CharField(max_length=20)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fullName
    
    class Meta:
        verbose_name_plural = "ContactUs"