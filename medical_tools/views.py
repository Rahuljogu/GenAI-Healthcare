import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@login_required
def symptom_checker_view(request):
    response_text = None
    symptoms = None

    if request.method == 'POST':
        symptoms = request.POST.get("symptoms")
        try:
            prompt = f"Analyze the following symptoms and suggest possible causes and actions: {symptoms}"
            response = model.generate_content(prompt)
            response_text = response.text
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "medical_tools/symptom_checker.html", {
        "response": response_text,
        "symptoms": symptoms
    })

@login_required
def drug_info_view(request):
    response_text = None
    condition = None

    if request.method == 'POST':
        condition = request.POST.get("condition")
        try:
            prompt = f"Suggest drugs and treatments for the condition: {condition}. Explain their use briefly."
            response = model.generate_content(prompt)
            response_text = response.text
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "medical_tools/drug_info.html", {
        "response": response_text,
        "condition": condition
    })
