from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import json

class HealthView(View):
    def get(self, request):
        return JsonResponse({"status": "ok", "service": "users"})

@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(View):
    def post(self, request):
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid json"}, status=400)
        username = payload.get("username")
        password = payload.get("password")
        if not username or not password:
            return JsonResponse({"error": "username and password required"}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "username taken"}, status=409)
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({"id": user.id, "username": user.username}, status=201)


