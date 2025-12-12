from django.db import models

class Cluster(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المشكلة المجمعة")
    category = models.CharField(max_length=100, default="عام", verbose_name="التصنيف الرئيسي")
    ai_summary = models.TextField(blank=True, verbose_name="ملخص الذكاء الاصطناعي (السؤال العام)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 👇 هذا الحقل الجديد
    is_approved = models.BooleanField(default=False, verbose_name="تم الاعتماد")

    def __str__(self):
        return self.title