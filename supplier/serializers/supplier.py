from rest_framework.serializers import ModelSerializer

from ..models import Supplier


class SupplierShortSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["name", "phone", "address"]


class SupplierCreateSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierFullSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["name", "phone", "email", "address"]
