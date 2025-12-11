from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket

def submit_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            
            # إعدادات تلقائية لا يراها المستخدم
            ticket.source = 'ABSHER'  # نحدد المصدر أنه من البوابة
            ticket.status = 'NEW'     # الحالة مبدئياً جديد
            
            # --- هنا سنضع كود استدعاء الـ AI لاحقاً ---
            # call_ai_engine(ticket)
            
            ticket.save()
            return render(request, 'main/success.html') # صفحة شكر
    else:
        form = TicketForm()
    
    return render(request, 'main/submit_ticket.html', {'form': form})


# backend/main/views.py

def success_page_view(request):
    return render(request, 'main/success.html')

