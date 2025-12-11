from django.db import models

# 1. المودل الخاص بتجميع المشاكل المتشابهة (للداشبورد)
class Cluster(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المشكلة المجمعة")
    # مثلاً: "مشكلة عامة في بوابة النفاذ الوطني"
    
    category = models.CharField(max_length=100, default="عام", verbose_name="التصنيف الرئيسي")
    # جوازات، مرور، تقنية...
    
    ai_summary = models.TextField(blank=True, verbose_name="ملخص الذكاء الاصطناعي")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 2. المودل الخاص بالحلول المقترحة (قاعدة المعرفة)
class Solution(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الحل")
    content = models.TextField(verbose_name="نص الحل المقترح")
    # نربط الحل بالمشكلة المجمعة بدلاً من التصنيف العام ليكون الحل أدق
    cluster = models.ForeignKey(Cluster, on_delete=models.SET_NULL, null=True, blank=True, related_name='solutions')
    
    def __str__(self):
        return self.title
# backend/main/models.py

class Ticket(models.Model):
    SOURCE_CHOICES = [
        ('ABSHER', 'بوابة أبشر'),
        ('TWITTER', 'منصة X (تويتر)'),
        ('EMAIL', 'البريد الإلكتروني'),
    ]
    
    STATUS_CHOICES = [
        ('NEW', 'جديد'),
        ('AI_PROCESSED', 'تم تحليله ذكياً'),
        ('USER_ACTION_REQUIRED', 'بانتظار رد المستفيد'),
        ('ESCALATED', 'مرفوع للموظف'),
        ('RESOLVED', 'تم الحل'),
    ]
    
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='ABSHER', verbose_name="المصدر")
    
    # 👇 هذا هو السطر الناقص عندك والذي يسبب المشكلة
    user_name = models.CharField(max_length=100, default="مجهول", verbose_name="اسم المستفيد")
    
    description = models.TextField(verbose_name="وصف المشكلة")
    ai_analysis = models.TextField(blank=True, null=True, verbose_name="تحليل الذكاء الاصطناعي")
    suggested_solution = models.TextField(blank=True, null=True, verbose_name="الحل المقترح")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='NEW', verbose_name="الحالة")
    
    # انتبه: إذا كنت تستخدم المودل المطور (مع Cluster)، تأكد من وجود حقل cluster هنا أيضاً
    # cluster = models.ForeignKey(Cluster, ... ) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.source}"

# 4. مودل التنبيهات
class Alert(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان التنبيه")
    message = models.TextField(verbose_name="رسالة التنبيه")
    level = models.CharField(max_length=20, choices=[('WARNING', 'تحذير'), ('CRITICAL', 'خطر')], default='WARNING')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.level})"