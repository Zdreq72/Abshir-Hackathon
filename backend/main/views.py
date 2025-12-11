from django.shortcuts import render
from django.http import JsonResponse
from .models import Ticket
from .ai_utils import get_absher_solution # تأكد أن هذا الملف موجود وفيه مفتاح API

def submit_ticket(request):
    if request.method == 'POST':
        # 1. هل هذا طلب جديد أم إعادة محاولة؟
        ticket_id = request.POST.get('ticket_id')
        
        if ticket_id:
            # --- سيناريو إعادة المحاولة (المستخدم لم يعجبه الحل) ---
            ticket = Ticket.objects.get(id=ticket_id)
            ticket.retry_count += 1
            
            if ticket.retry_count >= 3:
                # إذا وصل 3 محاولات -> تصعيد للموظف
                ticket.status = 'ESCALATED'
                ticket.save()
                return JsonResponse({
                    'status': 'escalated',
                    'message': 'نعتذر منك. تم رفع تذكرتك للموظف المختص نظراً لتكرار المحاولة، سيتم التواصل معك قريباً.'
                })
            else:
                # محاولة جديدة مع الـ AI (ربما يعطي إجابة مختلفة أو نطلب توضيح)
                # للتبسيط هنا: سنرسل نفس الحل أو نطلب صياغة أفضل، 
                # لكن الأفضل في الـ Production نرسل الـ History لـ Gemini.
                new_solution = get_absher_solution(ticket.description + " (محاولة ثانية، الحل السابق لم يكن مفيداً)")
                ticket.suggested_solution = new_solution
                ticket.save()
                
                return JsonResponse({
                    'status': 'retry',
                    'solution': new_solution,
                    'retry_count': ticket.retry_count,
                    'remaining': 3 - ticket.retry_count
                })

        else:
            # --- سيناريو طلب جديد (أول مرة) ---
            user_name = request.POST.get('user_name')
            description = request.POST.get('description')
            
            # إنشاء التذكرة
            ticket = Ticket.objects.create(
                user_name=user_name,
                description=description,
                source='ABSHER',
                status='AI_PROCESSED'
            )
            
            # استدعاء Gemini
            solution = get_absher_solution(description)
            ticket.suggested_solution = solution
            ticket.save()
            
            return JsonResponse({
                'status': 'success',
                'ticket_id': ticket.id,
                'solution': solution
            })

    # طلب GET عادي (فتح الصفحة)
    return render(request, 'main/submit_ticket.html')