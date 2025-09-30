from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Comment
import json

class HealthView(View):
    def get(self, request):
        return JsonResponse({"status": "ok", "service": "comments"})

@method_decorator(csrf_exempt, name="dispatch")
class CommentsView(View):
    def get(self, request):
        items = [model_to_dict(c) for c in Comment.objects.order_by("-created_at")[:50]]
        return JsonResponse({"results": items})

    def post(self, request):
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid json"}, status=400)
        author = payload.get("author", "anonymous")
        text = payload.get("text", "")
        if not text:
            return JsonResponse({"error": "text required"}, status=400)
        c = Comment.objects.create(author=author, text=text)
        return JsonResponse(model_to_dict(c), status=201)


