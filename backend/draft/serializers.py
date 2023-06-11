from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Item, Seller, Order

class ItemSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if data['total_stock'] < data['minimum_order']:
            raise ValidationError('Total stock should be greater than minimum order')
    
    class Meta:
        model = Item
        fields = '__all__'
        
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'