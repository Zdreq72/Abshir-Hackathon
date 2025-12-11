import google.generativeai as genai

API_KEY = "AIzaSyAmSh5aEsuF7pdHPsCCBRHg_NJBJzZ_N4k"

try:
    print("--- 1. الاتصال ---")
    genai.configure(api_key=API_KEY)
    
    # 👇 نستخدم الاسم الموجود في قائمتك
    model_name = 'gemini-flash-latest'
    
    print(f"--- 2. تجربة المودل: {model_name} ---")
    model = genai.GenerativeModel(model_name)
    
    response = model.generate_content("مرحباً، هل تعمل؟")
    print(f"✅ تم النجاح! الرد: {response.text}")

except Exception as e:
    print(f"❌ خطأ: {e}")