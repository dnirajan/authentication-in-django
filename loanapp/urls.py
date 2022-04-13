from django.contrib import admin
from django.urls import path
from loanapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                path('', views.index, name='index'),
                path('register/', views.register, name='register'),
                path('login/', views.userlogin, name='login'),
                path('profile/', views.userprofile, name='profile'),
                path('logout/', views.userlogout, name='logout'),
                path('changepass/', views.changepass, name='changepass'),
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
