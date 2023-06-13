from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Item, Seller, Order, Buyer

class ItemSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if data['total_stock'] < data['minimum_order']:
            raise ValidationError('Total stock should be greater than minimum order')
        return data
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
        

class BuyerSerializer(serializers.ModelSerializer):
    
    def validate_quantity(self, value):
        item = Item.objects.get(item_id=1) # Fetch the associated Item instance based on the condition
        if value < item.minimum_order or value >= item.total_stock:
            raise ValidationError('Invalid quantity')

        return value
    
    class Meta:
        model = Buyer
        fields = '__all__'