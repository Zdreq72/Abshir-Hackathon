from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('generator/', views.generator, name='generator'),
    path('library/', views.library, name='library'),
    # حذفنا سطر include('main.urls') من هنا لأنه مكانه غلط ❌
]