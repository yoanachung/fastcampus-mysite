from rest_framework import serializers
from order.models import Shop, Menu, Order, OrderFood

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'