from django.urls import path

from draw import views

urlpatterns = [
    path('toto_lotek/', views.toto_lotek)
]