"""
URL configuration for drfsite project.

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
from django.urls import path, include, re_path

from easyjob.views import *
from rest_framework import routers

# # создаем переменную с классом SimpleRouter
# router = routers.SimpleRouter()
# # регистрируем класс ViewSet
# router.register(r'freelancers', FreelancersViewSet, basename='freelancers')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/auth/', include('rest_framework.urls')),  # авторизация на основе сессий
    path('api/v1/freelancers/', FreelancersApiList.as_view()),  # api/v1/freelancers
    path('api/v1/freelancers/<int:pk>/', FreelancersApiUpdate.as_view()),
    path('api/v1/freelancersdelete/<int:pk>', FreelancersApiList.as_view()),
    path('api/v1/vacancies/', VacanciesApiList.as_view()),  # api/v1/freelancers
    path('api/v1/vacancies/<int:pk>/', VacanciesApiUpdate.as_view()),
    path('api/v1/vacanciesdelete/<int:pk>', VacanciesApiList.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
