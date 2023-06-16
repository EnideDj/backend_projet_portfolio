from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('#home/', views.homebis, name='#home'),
    path('#about/', views.aboutbis, name='#about'),
    path('#resume/', views.resumebis, name='#resume'),
    path('#portfolio/', views.portfoliobis, name='#portfolio'),
    path('#services/', views.servicesbis, name='#services'),
    path('#contact/', views.contactbis, name='#contact'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/home/', views.home, name='home'),
    path('accounts/profile/about/', views.about, name='about'),
    path('accounts/profile/resume/', views.resume, name='resume'),
    path('accounts/profile/portfolio/', views.portfolio, name='portfolio'),
    path('accounts/profile/services/', views.services, name='services'),
    path('accounts/profile/contact/', views.contact, name='contact'),
    path('accounts/profile/skills/', views.skills, name='skills'),
    
    path('', views.index, name='index'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
]