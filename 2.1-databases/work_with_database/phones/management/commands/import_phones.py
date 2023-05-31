import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            id = phone['id']
            name = phone['name']
            price = phone['price']
            image = phone['image']
            release_date = phone['release_date']
            lte_exists = phone['lte_exists']
            slug = slugify(name)

            phone_obj = Phone(id=id, name=name, price=price, image=image, release_date=release_date, lte_exists=lte_exists,
                              slug=slug)
            phone_obj.save()
