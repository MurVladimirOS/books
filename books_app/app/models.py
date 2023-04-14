from django.db import models


# Create your models here.


class AllBooks(models.Model):
    name = models.CharField(max_length=250, blank=True, null=False, verbose_name='Name')
    descriptions = models.CharField(max_length=250, blank=True, null=False, verbose_name='Descriptions')
    author = models.CharField(max_length=250, blank=True, null=False, verbose_name='Author')
    date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True, verbose_name="Date creating")
    count_page = models.PositiveIntegerField(verbose_name='count page', null=True, blank=True)
    date_manual = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name="Manual date")

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name
