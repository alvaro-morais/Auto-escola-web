from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Auto Escola Líder"

urlpatterns = [
    path('', views.home, name='home'),
    path('cliente', views.cliente, name='cliente'),
    path('login', views.login, name='login'),
    path('adm', views.adm, name='adm'),
    path('accounts/', include('django.contrib.auth.urls')),
]