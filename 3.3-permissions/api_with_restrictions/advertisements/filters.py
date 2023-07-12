from django_filters import rest_framework as filters

from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    min_date = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    max_date = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Advertisement
        fields = ['status', 'min_date', 'max_date']
