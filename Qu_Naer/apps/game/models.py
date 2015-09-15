#!/usr/bin/env python
#!-*-coding:utf-8-*-
__author__ = 'gong'
__create_time__ = '12/09/2015'


import datetime
from django.db import models
from django.forms.models import model_to_dict
from django.utils.timezone import utc


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=64, blank=True)
    game_alias = models.CharField(max_length=64, blank=True)
    initial_name = models.CharField(max_length=64, blank=True)
    developer_id = models.BigIntegerField(blank=True, null=True)
    publisher_id = models.BigIntegerField(blank=True, null=True)
    cover_image = models.CharField(max_length=32, blank=True)
    release_date = models.DateTimeField(blank=True, null=True)
    game_language = models.CharField(max_length=64, blank=True)
    game_brief = models.TextField(blank=True, null=True)
    game_space = models.CharField(max_length=16, blank=True)
    game_site = models.CharField(max_length=64, blank=True)
    game_level = models.CharField(max_length=16, blank=True)
    game_status = models.SmallIntegerField(blank=True, null=True)
    game_audit = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rdb_game'
        managed = True

    def __str__(self):
        return '%s, %s, %s, %s' % (self.game_id, self.game_name, self.game_status, game_audit)

    def canonical(self):
        """
        return the object as a tuple
        """
        fields = model_to_dict(self, fields=('game_id', 'game_name', 'game_alias', 'initial_name', 'developer_id',
                                             'publisher_id', 'cover_image', 'release_date','game_language','game_brief',
                                              'game_space','game_site', 'game_level'))
        return fields

    def canonical_trim_game(self):
        """
        trim game information for one game
        """
        fields = model_to_dict(self, fields=('game_id', 'game_name', 'initial_name', 'cover_image'))
        return fields

    def create_game(self, *args, **kwargs):
        self.game_status = '0'
        self.game_audit = '0'
        super(Game, self).save(*args, **kwargs)
        return self

    def get_one_game(self, game_id):
        return self.objects.get(game_id=game_id)

    def get_game_list(self, page_num):
        offset = (page_num-1)*9
        limit = 9
        ret = []
        queryset = self.objects.exclude(game_status='1')[offset,limit]
        for game in queryset:
            ret.append(game.game_id)
        return ret

    def get_total_num(self):
        total = self.objects.count()
        return total

    def update_game(self, game_id, **kwargs):
        self.objects.filter(game_id=game_id).update(**kwargs)

    def delete_game(self, game_id):
        self.objects.filter(id=game_id).update(game_status=1)


class Company(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_name = models.CharField(max_length=64, blank=True)
    comp_initial = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = 'rdb_company'
        managed = True

    def create_company(self, **kwargs):
        company = Company(comp_name = kwargs.get('company_name'))
        company.save()
        return self

    def get_company_by_id(self, **kwargs):
        return self.objects.get(comp_id = kwargs.get('company_id'))

    def get_company_by_name(self, company_name):
        return self.objects.get(comp_name = company_name)

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=64,blank=False)

    class Meta:
        db_table = 'rdb_type'
        managed = True

    def create_type(self, **kwargs):
        typ = Type(type_name = kwargs.get('type_name'))
        typ.save()
        return self

    def get_type(self, **kwargs):
        return self.objects.get(type_id = kwargs.get('type_id'))

class GameType(models.Model):
    game_id = models.BigIntegerField(blank=True, null=True)
    type_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rdb_gtype'
        managed = True

    def insert_relationship(self, **kwargs):
        relation = GameType(game_id = kwargs.get('game_id'),
                            type_id =kwargs.get('type_id'))
        relation.save()
        return self

    def get_game_type(self, game_id):
        return self.objects.filter(game_id = game_id)

    def get_games_by_type(self, type_id):
        return self.objects.filter(type_id = type_id)

class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=32,blank=False)

    class Meta:
        db_table = 'rdb_platform'
        managed = True

    def create_platform(self, **kwargs):
        platform = Platform(platform_name = kwargs.get('platform_name'))
        platform.save()
        return self

    def get_platform(self, **kwargs):
        return self.objects.get(platform_id = kwargs.get('platform_id'))

class GamePlatform(models.Model):
    game_id = models.BigIntegerField(blank=True, null=True)
    platform_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rdb_gplatform'
        managed = True

    def insert_relationship(self, **kwargs):
        relation = GamePlatform(game_id = kwargs.get('game_id'),
                                platform_id =kwargs.get('platform_id'))
        relation.save()
        return self

    def get_game_platform(self, game_id):
        return self.objects.filter(game_id = game_id)

    def get_games_by_platform(self, platform_id):
        return self.objects.filter(platform_id = platform_id)

