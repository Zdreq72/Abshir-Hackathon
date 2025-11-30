from django.urls import path
from . import views

app_name = 'dashboard'  # مهم جداً للـ Namespacing

urlpatterns = [
    path('', views.home, name='home'),
    path('generator/', views.generator, name='generator'),
    path('library/', views.library, name='library'),
    
]