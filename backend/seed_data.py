import os
import django
import random

# إعداد بيئة جانغو
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SolutionHub.settings')
django.setup()

from dashboard.models import Cluster

def create_fake_data():
    print("جاري حذف البيانات القديمة...")
    Cluster.objects.all().delete()

    titles = [
        "مشكلة في تفعيل الهوية الرقمية",
        "عدم وصول رمز التحقق (OTP)",
        "طريقة تجديد الجواز لمن هم دون 15 سنة",
        "خطأ 403 عند الدخول للنفاذ الوطني",
        "استفسار بخصوص المخالفات المرورية",
        "تحديث البيانات الوظيفية لا يعمل",
    ]
    
    sources = ["Twitter", "Call Center", "Chatbot", "Email"]

    print("جاري إضافة بيانات جديدة...")
    for title in titles:
        Cluster.objects.create(
            title=title,
            count=random.randint(50, 500),
            confidence=random.randint(70, 99),
            source=random.choice(sources)
        )
    
    print("✅ تم إضافة البيانات بنجاح! قم بتحديث الصفحة الآن.")

if __name__ == '__main__':
    create_fake_data()