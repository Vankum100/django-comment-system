from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView, comments_page, feedback_view, get_new_comments, home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("", home_view, name="home"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("feedback/", feedback_view, name="feedback"),
    path("comments/", comments_page, name="comments_page"),
    path("get_new_comments/", get_new_comments, name="get_new_comments"),
]


