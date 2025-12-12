from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # الصفحة الرئيسية = فورم تقديم الشكوى
    path('', views.submit_ticket, name='home'), 
    
    path('submit-ticket/', views.submit_ticket, name='submit_ticket'),
    # path('ticket-result/<int:ticket_id>/', views.ticket_result, name='ticket_result'),
]