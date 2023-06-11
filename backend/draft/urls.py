from rest_framework import routers

from . import views

app_name = 'draft'

router = routers.DefaultRouter()
router.register('items', views.ItemViewSet)
router.register('sellers', views.SellerViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = router.urls