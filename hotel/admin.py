from django.contrib import admin

# Register your models here.
from .models import User, ContactUs, Roombook

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('id','username','first_name','last_name','email','contact')
    list_display_links = ('username',)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_per_page = 30

@admin.register(ContactUs)
class AdminContactUs(admin.ModelAdmin):
    list_display = ('id','fullName','email','subject')
    search_fields = ('fullName','email')
    list_per_page = 25

@admin.register(Roombook)
class AdminRoombook(admin.ModelAdmin):
    list_display = ('id','user','arrival_date','days','number_of_guests')
    search_fields = ('user','arrival_date')
    list_per_page = 25