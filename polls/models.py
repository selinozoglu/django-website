import datetime

import django
from django.db import models

SUC = 'Suç'
CEZA = 'Ceza'
SUCD = 'Suç Değil'
HUKUK = 'Hukuk'

choice = [SUC, CEZA, SUCD, HUKUK]

TYPE_CHOICES = [
    (SUC, 'Suç'),
    (CEZA, 'Ceza'),
    (SUCD, 'Suç Değil'),
    (HUKUK, 'Hukuk')
]


class Makale(models.Model):
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=SUC, null=False, blank=False, verbose_name='makalenin tipi')
    title = models.CharField(max_length=200, verbose_name='makale başlık', null=False, blank=False, default="Baslık")
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=300, verbose_name='makale açıklama', null=False, blank=False, default="makale açıklama")
    text = models.TextField(verbose_name='içerik', null=False, blank=False)
    publish_date = models.DateField(verbose_name='yayınlanma zamanı', default=django.utils.timezone.now)
    isVisible = models.BooleanField(verbose_name='makale yayınlansın mı', null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Slide(models.Model):
    text = models.TextField(verbose_name='içerik', null=False, blank=False)
    title = models.CharField(max_length=100, verbose_name='makale başlık', null=False, blank=False, default="Baslık")

    def __str__(self):
        return self.title
