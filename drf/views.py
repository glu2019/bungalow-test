from drf.models import Bungalow
from drf.serializers import BungalowSerializer
from drf.filters import BungalowFilter
from drf.pagination import ClientSetPagination
from rest_framework import viewsets


class BungalowViewSet(viewsets.ModelViewSet):
    queryset = Bungalow.objects.all()
    serializer_class = BungalowSerializer
    pagination_class = ClientSetPagination
    filter_class = BungalowFilter