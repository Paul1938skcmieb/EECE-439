from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('all-contacts/', views.all_contacts, name='all_contacts'),
]
