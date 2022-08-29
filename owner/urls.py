from django.urls import path
from owner import views

app_name = 'owner'
urlpatterns = [
    path('orders/<int:shop>', views.orders, name="orders"),
    path('accept/', views.accept, name="accept"),
]