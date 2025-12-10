from django.shortcuts import render
from .models import Cluster
from django.shortcuts import get_object_or_404

def home(request):
    # جلب جميع المشاكل مرتبة بالأكثر تكراراً
    clusters = Cluster.objects.all().order_by('-count')
    context = {
        'clusters': clusters,
        'total_count': sum(c.count for c in clusters), # حساب إجمالي الاستفسارات
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