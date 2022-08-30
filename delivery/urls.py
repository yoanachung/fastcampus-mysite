from django.urls import path
from delivery import views

app_name = 'delivery'
urlpatterns = [
    path('orders/', views.orders, name="orders"),
]