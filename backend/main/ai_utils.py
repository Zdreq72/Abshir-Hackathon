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
        أنت مساعد دعم فني ذكي لمنصة "أبشر" السعودية.

        قواعد الرد المهمة:
        - إذا كانت رسالة المستخدم تحية فقط (مثل: مرحبا، أهلاً، كيف الحال):
        • رد بتحية سعودية رسمية قصيرة فقط
        • لا تذكر تحليل مشكلة
        • لا تستخدم عناوين أو نقاط
        • اطلب من المستخدم توضيح طلبه بجملة واحدة

        - إذا كانت رسالة المستخدم تحتوي على مشكلة أو استفسار تقني:
        • حلّل المشكلة باختصار
        • قدّم حلاً واضحاً ومباشراً
        • استخدم لهجة سعودية رسمية ومطمئنة
        • لا تطِل في الشرح
        • لا تكرر التحية أكثر من مرة

        - لا تبدأ الرد بجمل مثل:
        "بصفتي خبيراً"
        "تحليل المشكلة"
        "اقتراح الحل"

        - اجعل الرد طبيعي كموظف دعم حقيقي في أبشر.

        رسالة المستخدم:
        "{problem_text}"
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return "عذراً، النظام يواجه ضغطاً حالياً. تم رفع طلبك للموظف المختص."
