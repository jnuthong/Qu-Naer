#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '02/04/2014'

from django.db import models


class Geography(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    longitude = models.BigIntegerField(null=True, blank=True)
    latitude = models.BigIntegerField(null=True, blank=True)
    status = models.SmallIntegerField(null=True, blank=True, default=0)

    class Meta:
        db_table = 'rdb_geography'
        managed = True

    def __str__(self):
        return '%s, %s, %s, %s' % (self.id, self.city, self.longitude, self.latitude)

    def create_geo_info(self, *args, **kwargs):
        super(Geography, self).save(*args, **kwargs)
        return self

    def get_geo_info(self, geo_id):
        return self.objects.get(id=geo_id)

    def filter_by_city(self, city):
        return self.objects.filter(city=city)

