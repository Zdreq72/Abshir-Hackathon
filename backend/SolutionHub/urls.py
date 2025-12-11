from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. روابط الداشبورد (أي رابط يبدأ بـ dashboard/ يروح لتطبيق الداشبورد)
    path('dashboard/', include('dashboard.urls')),
    
    # 2. روابط الموقع الرئيسي والفورم (أي رابط ثاني يروح للـ main)
    path('', include('main.urls')),
]