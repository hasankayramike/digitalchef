"""
URL configuration for digitalchef project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("meal_planner.urls")),
    path("register/", user_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('choose-diet/', user_views.diet_form_view, name='diet_form'),
    path('allergies/', user_views.allergy_form_view, name='allergy_form'),
    path('personal_information/', user_views.personal_information_form_view, name='personal_information_form'),
    path("profile/", user_views.profile, name="profile"),
    path("meal_plan/", user_views.query_view, name="meal_plan"),
]

