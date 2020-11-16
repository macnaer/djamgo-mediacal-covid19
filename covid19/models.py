from django.db import models


class covid19(models.Model):
    country = models.CharField(max_length=128)
    countrycode = models.CharField(max_length=10)
    slug = models.CharField(max_length=128)
    newconfirmed = models.IntegerField()
    totalconfirmed = models.IntegerField()
    totaldeaths = models.IntegerField()
    newrecovered = models.IntegerField()
    totalrecovered = models.IntegerField()

    class Meta:
        verbose_name = 'covid19'
        verbose_name_plural = 'covid19s'
