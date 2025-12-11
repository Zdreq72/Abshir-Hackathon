from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [

    path('', views.submit_ticket, name='home'),
    # رابط الفورم
    path('submit-ticket/', views.submit_ticket, name='submit_ticket'),
    
    # صفحة النجاح
    path('success/', views.success_page_view, name='success'),
]