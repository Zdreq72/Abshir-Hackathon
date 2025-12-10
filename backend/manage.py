#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import random # تأكد أنك سويت استيراد لهذه المكتبة فوق في بداية الملف


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SolutionHub.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#عشان اخطاء الي بتظهر في html 
# ... بقية الكلاس
    
    @property
    def color_code(self):
        if self.confidence > 80:
            return "#00b894"
        elif self.confidence > 60:
            return "#fdcb6e"
        else:
            return "#ff7675"
        



# ... داخل كلاس Cluster

    @property
    def supported_languages(self):
        # هذه الدالة تحاكي أن النظام يدعم لغات مختلفة لكل حل
        # مثلاً بعض الحلول تدعم العربية والانجليزية، وبعضها يدعم الأوردو أيضاً
        langs = [
            {'code': 'AR', 'name': 'العربية', 'flag': '🇸🇦'},
            {'code': 'EN', 'name': 'English', 'flag': '🇺🇸'},
            {'code': 'UR', 'name': 'Urdu', 'flag': '🇵🇰'},
            {'code': 'TL', 'name': 'Tagalog', 'flag': '🇵🇭'},
        ]
        # اختيار لغات عشوائية (دائماً العربية موجودة + 1 أو 2 لغة إضافية)
        available = [langs[0]] + random.sample(langs[1:], k=random.randint(1, 2))
        return available