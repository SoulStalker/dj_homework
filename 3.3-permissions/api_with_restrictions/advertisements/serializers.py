from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at',)

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user

        if self.instance and self.instance.creator != user:
            raise serializers.ValidationError("Вы не можете изменять это объявление.")

        if self.context['request'].method == 'POST' or data.get('status') == AdvertisementStatusChoices.OPEN:
            open_ads_count = Advertisement.objects.filter(creator=user, status=AdvertisementStatusChoices.OPEN).count()
            if open_ads_count >= 10:
                raise serializers.ValidationError("Превышено ограничение на количество открытых объявлений.")

        return data