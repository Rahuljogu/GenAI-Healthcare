import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import ChatLog

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@login_required
def chat_view(request):
    response_text = None
    user_prompt = None

    if request.method == 'POST':
        user_prompt = request.POST.get("prompt")
        try:
            # Use Gemini Flash 2.5 to generate response
            response = model.generate_content(user_prompt)
            response_text = response.text

            # ✅ Save to database inside POST block
            if user_prompt and response_text:
                ChatLog.objects.create(
                    user=request.user,
                    prompt=user_prompt,
                    response=response_text
                )

        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "ai_assistant/chat.html", {
        "response": response_text,
        "user_prompt": user_prompt
    })
