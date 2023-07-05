from django.contrib import admin

from .models import Advertisement


@admin.register(Advertisement)
class AdminAdvertisement(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']


