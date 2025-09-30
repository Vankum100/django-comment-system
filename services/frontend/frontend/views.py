from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import os
import requests

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def comments_page(request):
    base_url = os.environ.get("COMMENTS_BASE_URL", "http://127.0.0.1:8002")
    api_url = f"{base_url}/api/comments/"
    if request.method == "POST":
        author = request.user.username if request.user.is_authenticated else "anonymous"
        text = request.POST.get("text", "").strip()
        if text:
            try:
                requests.post(api_url, json={"author": author, "text": text}, timeout=5)
            except Exception:
                pass
        return redirect("comments_page")
    
    # Show only current user's comments
    items = []
    if request.user.is_authenticated:
        try:
            r = requests.get(api_url, timeout=5)
            data = r.json()
            all_comments = data.get("results", [])
            items = [c for c in all_comments if c.get("author") == request.user.username]
        except Exception:
            items = []
    return render(request, "comments_page.html", {"items": items})


def home_view(request):
    # Show all comments from all users on the main page
    base_url = os.environ.get("COMMENTS_BASE_URL", "http://127.0.0.1:8002")
    api_url = f"{base_url}/api/comments/"
    all_comments = []
    try:
        r = requests.get(api_url, timeout=5)
        data = r.json()
        all_comments = data.get("results", [])
    except Exception:
        all_comments = []
    return render(request, "home.html", {"all_comments": all_comments})


def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "anonymous").strip() or "anonymous"
        message = request.POST.get("message", "").strip()
        if message:
            token = settings.TELEGRAM_BOT_TOKEN
            chat_id = settings.TELEGRAM_CHAT_ID
            if token and chat_id:
                url = f"https://api.telegram.org/bot{token}/sendMessage"
                text = f"Feedback from {name}:\n{message}"
                try:
                    requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=5)
                except Exception:
                    pass
        return redirect("feedback")
    return render(request, "feedback.html")


def get_new_comments(request):
    last_id = request.GET.get("last_id")
    base_url = os.environ.get("COMMENTS_BASE_URL", "http://127.0.0.1:8002")
    api_url = f"{base_url}/api/comments/"
    try:
        r = requests.get(api_url, timeout=5)
        data = r.json()
        items = data.get("results", [])
        if last_id is not None:
            try:
                last_id_int = int(last_id)
                items = [c for c in items if int(c.get("id", 0)) > last_id_int]
            except ValueError:
                pass
        return JsonResponse({"results": items})
    except Exception:
        return JsonResponse({"results": []})


