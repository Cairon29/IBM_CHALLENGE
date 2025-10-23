from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import json

@csrf_exempt
def home(request):
    return render(request, "index.html")

@csrf_exempt
def analyze_text(request):
    summary_result = None


    message = None
    uploaded_file = None
    
    if request.content_type == 'application/json':
        data = json.loads(request.body)
        print(data)
        message = data.get('message', '')
        uploaded_file = None
    else:
        message = request.POST.get('message', '')
        uploaded_file = request.FILES.get('file')

    text_valid_extensions = ('.txt', '.csv')

    if uploaded_file:
        if not uploaded_file.name.lower().endswith(text_valid_extensions):
            return JsonResponse({"error": "Invalid file extension. Only TXT, and CSV are allowed."}, status=415)
        
    try:
        uploaded_file = request.FILES.get('file')

        if uploaded_file and message is None:
            return JsonResponse({"error": "No file nor text was given in the request"}, status=406)
        if not uploaded_file.name.lower().endswith(text_valid_extensions):
            return JsonResponse({"error": "File must be a TXT file."}, status=415)
        
        text = uploaded_file.read().decode('utf-8')
        text = None

        if message:
            text = message
        if uploaded_file:
            text = uploaded_file.read().decode('utf-8')

        from .sum import summarizer_wrapper
        summarizer = summarizer_wrapper().summarizer()
        summary = summarizer(
            text, max_length=100, min_length=30, do_sample=False
        )
        summary_result = summary[0]["summary_text"]
        return JsonResponse({
            "summary_result": summary_result,
            # "classification_result": classification_result
        }, status=200)
    except Exception as e:
        return JsonResponse({"error": "Error processing the file."}, status=500)