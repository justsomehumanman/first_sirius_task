from django.urls import path, include
from . import views

urlpatterns = [
    path('shorten/', views.LinkPost.as_view()),
    path('<str:get_token>/views/', views.LinkViewGet.as_view()),
    path('<str:get_token>/', views.LinkGet.as_view()),
]
