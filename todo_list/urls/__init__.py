"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from todo_list.views import (
    GoogleLogin,
    TodoListCreateAPIView,
    TodoRetrieveUpdateDestroyAPIView,
)

from django.http import HttpResponse


def return_auth_code(request):
    return HttpResponse(request.GET.get("code"))


urlpatterns = [
    path("oauth2/callback/", return_auth_code, name="callback-url"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("dj-rest-auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("todos/", TodoListCreateAPIView.as_view(), name="todo-list-create"),
    path(
        "todos/<str:pk>/",
        TodoRetrieveUpdateDestroyAPIView.as_view(),
        name="todo-retrieve-update-destroy",
    ),
]
