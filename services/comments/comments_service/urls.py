from django.contrib import admin
from django.urls import path
from .views import HealthView, CommentsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", HealthView.as_view()),
    path("api/comments/", CommentsView.as_view()),
]


