from django.db import models

# 1. المودل الخاص بتجميع المشاكل (Clusters)
class Cluster(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المشكلة المجمعة")
    category = models.CharField(max_length=100, default="عام", verbose_name="التصنيف الرئيسي")
    ai_summary = models.TextField(blank=True, verbose_name="ملخص الذكاء الاصطناعي")
    
    # 👇 هذا الحقل كان ناقصاً وهو سبب المشكلة الحالية
    is_approved = models.BooleanField(default=False, verbose_name="تم الاعتماد")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 2. المودل الخاص بالحلول (Solutions)
class Solution(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الحل")
    content = models.TextField(verbose_name="نص الحل المقترح")
    cluster = models.ForeignKey(Cluster, on_delete=models.SET_NULL, null=True, blank=True, related_name='solutions')
    
    def __str__(self):
        return self.title

# 3. مودل التذكرة (Ticket)
class Ticket(models.Model):
    SOURCE_CHOICES = [
        ('TWITTER', 'Twitter'),
        ('CHATBOT', 'Chatbot'),
        ('CALL_CENTER', 'Call Center'),
        ('EMAIL', 'Email'),
        ('ABSHER', 'Absher Portal'),
    ]
    
    STATUS_CHOICES = [
        ('NEW', 'جديد'),
        ('AI_PROCESSED', 'تم تحليله ذكياً'),
        ('SOLVED', 'تم الحل'),
        ('ESCALATED', 'مرفوع للموظف'),
    ]

    # علاقة واحدة فقط (تم حذف التكرار)
    cluster = models.ForeignKey(Cluster, related_name='tickets', on_delete=models.SET_NULL, null=True, blank=True)
    
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='ABSHER', verbose_name="المصدر")
    user_name = models.CharField(max_length=100, default="مجهول", verbose_name="اسم المستفيد")
    description = models.TextField(verbose_name="نص الشكوى")
    
    # حقول الذكاء الاصطناعي
    confidence_score = models.IntegerField(default=0, verbose_name="نسبة الثقة") 
    ai_analysis = models.TextField(blank=True, null=True, verbose_name="تحليل AI")
    suggested_solution = models.TextField(blank=True, null=True, verbose_name="الحل المقترح")
    
    # حقول التكرار
    retry_count = models.IntegerField(default=0, verbose_name="عدد المحاولات")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='NEW', verbose_name="الحالة")
    
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