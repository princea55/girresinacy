
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import ConfirmPasswordresetform
urlpatterns = [
    path("", views.home, name="home"),
    path("about_us", views.about, name="about"),
    path("services", views.services, name="services"),
    path("apartment_rooms", views.rooms, name="rooms"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("privacy1", views.privacy, name="privacy"),
   


    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

    #social account login google
    path('social-auth/', include('social_django.urls', namespace="social")),

    #password reset
    path("password_reset/",views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),      
]