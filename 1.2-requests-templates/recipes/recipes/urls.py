from django.urls import path
from calculator.views import calculate_view

urlpatterns = [
    path('<dish_get>/', calculate_view, name='calculate')
]
