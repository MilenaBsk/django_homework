from django.urls import path
from my_calculator import views

urlpatterns = [
    path('calculator/', views.calculator),
    path('add/<value1>/<value2>/', views.add),
    path('substract/<value1>/<value2>/', views.substract),
    path('multiply/<value1>/<value2>/', views.multiply),
    path('divide/<value1>/<value2>/', views.divide),

]