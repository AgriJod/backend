from rest_framework import viewsets, permissions
from . import serializers
from .models import Item, Seller, Order

class ItemViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Item.objects.all()
    
class SellerViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.SellerSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Seller.objects.all()
    
class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Order.objects.all()