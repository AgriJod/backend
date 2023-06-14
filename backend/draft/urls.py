from rest_framework import routers

from . import views

app_name = 'draft'

router = routers.DefaultRouter()
router.register('items', views.ItemViewSet)
router.register('sellers', views.SellerViewSet)
router.register('orders', views.OrderViewSet)
router.register('buyers', views.BuyerViewSet)
router.register('buyers/<int:pk>/item_selection/', views.BuyerViewSet)
router.register('item_selections', views.ItemSelectionViewSet)


urlpatterns = router.urls