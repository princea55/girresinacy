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

numbers_of_days = (
    ("1", "1"),
    ('2',"2"),
    ('3', "3"),
    ('4', "4"),
    ('5', "5"),
    ('6', "6"),
)

class Roombook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roombook')
    arrival_date = models.DateField(null=False)
    days = models.CharField(max_length=10, choices=numbers_of_days, null=False)
    number_of_guests = models.CharField(max_length=10, null=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "Roombook"

