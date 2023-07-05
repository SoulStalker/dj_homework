from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy", "favorites"]:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, *args, **kwargs):
        """Удаление объявления."""
        instance = self.get_object()
        user = request.user

        if instance.creator != user:
            return Response(status=403, data={"detail": "Вы не можете удалять это объявление."})

        self.perform_destroy(instance)
        return Response(status=204)

    @action(detail=True, methods=['post'])
    def favorites(self, request, pk=None):
        """Добавление/удаление объявления в избранное."""
        instance = self.get_object()
        user = request.user

        if instance.creator == user:
            return Response(status=400, data={"detail": "Вы не можете добавить свое объявление в избранное."})

        if instance.favorites.filter(pk=user.pk).exists():
            instance.favorites.remove(user)
            return Response(status=200, data={"detail": "Объявление удалено из избранного."})
        else:
            instance.favorites.add(user)
            return Response(status=200, data={"detail": "Объявление добавлено в избранное."})
