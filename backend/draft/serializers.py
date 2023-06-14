from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Item, Seller, Order, Buyer, ItemSelection

class ItemSerializer(serializers.ModelSerializer):
    
    
    def validate(self, data):
        if data['total_stock'] < data['minimum_order']:
            raise ValidationError('Total stock should be greater than minimum order')
        return data
    class Meta:
        model = Item
        fields = '__all__'
        
class ItemSelectionSerializer(serializers.ModelSerializer):
    
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    
    
    def validate_quantity(self, value):       
        item = self.initial_data.get('item')
        
        if item:
            item_instance = Item.objects.get(pk=item)
            if value < item_instance.minimum_order or value > item_instance.total_stock:  # Compare quantity with MOA
                raise serializers.ValidationError("Quantity should be greater than or equal to the MOA.")
        return value

    class Meta:
        model = ItemSelection
        fields = ('item_selection_id', 'item', 'quantity')
        
class SellerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Seller
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        

class BuyerSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Buyer
        fields = '__all__'