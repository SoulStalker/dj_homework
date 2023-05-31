from django.db import models
from django.urls import reverse


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'Название', max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phone_images/')
    release_date = models.DateField(u'Дата релиза')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('name', kwargs={'slug': self.slug})
