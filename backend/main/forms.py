from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # المستخدم يعبئ فقط الاسم ووصف المشكلة
        fields = ['user_name', 'description']
        
        # تنسيق الحقول باستخدام Bootstrap لتظهر بشكل جميل
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'الاسم الثلاثي (اختياري)',
                'style': 'direction: rtl;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'اكتب تفاصيل المشكلة هنا... مثال: لا أستطيع تجديد الجواز وتظهر لي رسالة خطأ',
                'style': 'direction: rtl;'
            }),
        }
        
        labels = {
            'user_name': 'اسم المستفيد',
            'description': 'وصف المشكلة',
        }