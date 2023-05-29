from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ..models import Supplier
from ..serializers import (
    SupplierShortSerializer,
    SupplierCreateSerializer,
    SupplierFullSerializer,
)


class SupplierViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Supplier.objects.all()
    serializer_class = SupplierFullSerializer
    permission_classes = [AllowAny]

    http_method_names = ["get", "put", "patch", "post", "delete"]

    def get_serializer_class(self):
        if self.action in ("create", "put", "patch"):
            return SupplierCreateSerializer
        if self.action == "list":
            return SupplierShortSerializer
        if self.action == "retrieve":
            return SupplierFullSerializer
        return self.serializer_class
