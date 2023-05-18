from django.urls import path

from businesscard import views

urlpatterns = [
    path('', views.businesscard),

    ]