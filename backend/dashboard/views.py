from django.shortcuts import render
from main.models import Cluster
from django.shortcuts import get_object_or_404
from main.models import Ticket
from django.db.models import Count, Q
from django.shortcuts import redirect

def approval_queue(request):
    # التعامل مع أزرار القبول والرفض
    if request.method == 'POST':
        cluster_id = request.POST.get('cluster_id')
        action = request.POST.get('action')
        
        cluster = get_object_or_404(Cluster, id=cluster_id)
        
        if action == 'approve':
            cluster.is_approved = True
            cluster.save()
            # هنا ممكن تضيف رسالة نجاح
        elif action == 'reject':
            cluster.delete() # حذف المشكلة
            # هنا ممكن تضيف رسالة حذف
            
        return redirect('dashboard:approval_queue')

    # جلب المشاكل المعلقة (التي لم تعتمد) مع عدد التذاكر فيها
    pending_clusters = Cluster.objects.annotate(
        num_tickets=Count('tickets')
    ).filter(is_approved=False).order_by('-num_tickets')

    return render(request, 'dashboard/approval_queue.html', {'clusters': pending_clusters})

def home(request):
    # 1. جلب المشاكل التي تكررت أكثر من 50 مرة (Trend)
    # ملاحظة: للهاكاثون، غير الرقم 50 إلى 3 أو 5 عشان يشتغل العرض قدام الحكام 😉
    trending_threshold = 50 
    
    trending_clusters = Cluster.objects.annotate(
        num_tickets=Count('tickets')
    ).filter(num_tickets__gte=trending_threshold).order_by('-num_tickets')

    # 2. جلب التذاكر المرفوعة (التي فشل فيها الـ AI 3 مرات)
    escalated_tickets = Ticket.objects.filter(status='ESCALATED').order_by('-updated_at')

    context = {
        'trending_clusters': trending_clusters,   # المشاكل الشائعة (>50)
        'escalated_tickets': escalated_tickets,   # المشاكل الصعبة (3 محاولات)
        # ... باقي السياق القديم ...
    }
    return render(request, 'dashboard/index.html', context)



def generator(request):
    # نأخذ الـ ID من الرابط، مثلاً ?id=5
    cluster_id = request.GET.get('id')
    cluster = None
    if cluster_id:
        cluster = get_object_or_404(Cluster, id=cluster_id)
    
    return render(request, 'dashboard/generator.html', {'cluster': cluster})

def library(request):
    # هنا يفترض نجيب الحلول المعتمدة (مؤقتا نجيب كل الكلسترز)
    clusters = Cluster.objects.all()
    return render(request, 'dashboard/library.html', {'clusters': clusters})