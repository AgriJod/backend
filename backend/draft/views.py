from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
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
    
    @action(detail=False, methods=['GET'])
    def waiting_for_seller(self, request):
        orders = self.get_queryset().filter(payment_status='Waiting for Seller')
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)