from django.urls import path
from membre import views

urlpatterns = [
    path('listes/', views.listemedia, name="listes_media")
]