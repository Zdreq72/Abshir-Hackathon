import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. تحميل متغيرات البيئة
load_dotenv()

# 2. جلب المفتاح من الملف المخفي
API_KEY = os.getenv("GEMINI_API_KEY")

# تهيئة مفتاح API مرة واحدة
genai.configure(api_key=API_KEY)

# اسم موديل مدعوم فعليًا
MODEL_NAME = "gemini-flash-latest"

def get_absher_solution(problem_text) -> str:
    """
    هذه الدالة تتولى إرسال رسالة المستخدم إلى Gemini
    وتعيد النص الناتج — أو رسالة بديلة عند حدوث خطأ.
    """

    try:
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = f"""
        تصرف كخبير دعم فني في نظام 'أبشر' السعودي.
        لديك شكوى من مستخدم نصها: "{problem_text}"
        
        المطلوب:
        1. تحليل المشكلة وتحديد السبب.
        2. اقتراح حل تقني دقيق ومختصر.
        3. الرد بلهجة سعودية رسمية ومطمئنة.
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return "عذراً، النظام يواجه ضغطاً حالياً. تم رفع طلبك للموظف المختص."
