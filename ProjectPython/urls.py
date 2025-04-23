from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # Главная страница: список курсов
    path('<int:course_id>/', views.course_detail, name='course_detail'),  # Страница одного курса
    path('<int:course_id>/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),  # Урок курса
]
