from django.shortcuts import render
from transformers import pipeline

# Load both models once at startup
classifier = pipeline(
    "zero-shot-classification",
    model="joeddav/xlm-roberta-large-xnli"
)

summarizer = pipeline(
    "summarization",
    model="LeoCordoba/beto2beto-mlsum"
)


def analyze_text(request):
    classification_result = None
    summary_result = None

    if request.method == "POST":
        text = request.POST.get("text")

        if text:
            # Classification
            label_map = {
                "security problem": "security",
                "environmental problem": "environment",
                "education problem": "education",
                "health problem": "health"
            }

            classification = classifier(
                text, candidate_labels=list(label_map.keys())
            )
            predicted_label = classification["labels"][0]
            classification_result = label_map[predicted_label]

            # Summarization
            summary = summarizer(
                text, max_length=100, min_length=30, do_sample=False
            )
            summary_result = summary[0]["summary_text"]

    return render(request, "home.html", {
        "classification_result": classification_result,
        "summary_result": summary_result
    })
