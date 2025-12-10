from django.db import models

class Cluster(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المشكلة")
    count = models.IntegerField(default=1, verbose_name="عدد التكرار")
    confidence = models.IntegerField(default=80, verbose_name="ثقة AI")
    source = models.CharField(max_length=100, default="تويتر", verbose_name="المصدر")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title