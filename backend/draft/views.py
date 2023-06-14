from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers
from .models import *

class ItemViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Item.objects.all()
    
class ItemSelectionViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ItemSelectionSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ItemSelection.objects.all()
    
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


class BuyerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BuyerSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Buyer.objects.all()
    
    @action(detail=True, methods=['get'])
    def item_selection(self, request, pk=None):
        buyer = self.get_object()
        items = Item.objects.all()
        item_data = serializers.ItemSerializer(items, many=True).data
        return Response(item_data)
    
    
