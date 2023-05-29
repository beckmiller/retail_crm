from django.urls import path, include
from rest_framework import routers

from .views import SupplierViewSet

router = routers.DefaultRouter()
router.register("supplier", SupplierViewSet, "supplier")

urlpatterns = [path("", include(router.urls))]
