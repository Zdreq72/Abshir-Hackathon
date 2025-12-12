from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('generator/', views.generator, name='generator'),
    path('library/', views.library, name='library'),
    path('approval/', views.approval_queue, name='approval_queue'),
    # حذفنا سطر include('main.urls') من هنا لأنه مكانه غلط ❌
]