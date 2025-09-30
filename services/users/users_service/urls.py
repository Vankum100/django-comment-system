from django.contrib import admin
from django.urls import path
from .views import HealthView, RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", HealthView.as_view()),
    path("api/register/", RegisterView.as_view()),
]


