# -*- coding: utf-8 -*-
__author__ = 'Gong'

from django.db import models
from django.utils.encoding import smart_str

class Auction(models.Model):
    auction_id = models.AutoField(primary_key=True, unique=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    place_id = models.BigIntegerField(blank=True, null=True)
    stuff_name = models.CharField(max_length=32, blank=True)
    stuff_describe = models.TextField(blank=True, null=True)
    stuff_image = models.CharField(max_length=32, blank=True)
    stuff_type = models.SmallIntegerField(blank=True, null=True)
    start_price = models.DecimalField(max_digits=11, decimal_places=2) #The crash may occur when decimal convert to float !
    instant_price = models.DecimalField(max_digits=11, decimal_places=2) #The crash may occur when decimal convert to float !
    create_time = models.DateTimeField(blank=True,
                                         null=True,
                                         auto_now_add=True)
    update_time = models.DateTimeField(blank=True,
                                         null=True,
                                         auto_now=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    stuff_status = models.SmallIntegerField(default=1, null=True) # 1.upcoming, 2.auctioning, 3.complete, 4.other...
    stuff_audit = models.SmallIntegerField(default=1, null=True)

    class Meta:
        db_table = 'rdb_auction'
        index_together = [
            ["user_id"],
            ["auction_id"],
            ["place_id"],
            ["stuff_type"],
        ]

    def __str__(self):
        return smart_str("%s, %s" % ( self.auction_id, self.user_id))

    def __unicode__(self):
        return u"%s, %s" % ( self.auction_id, self.user_id)

    def create_auction(cls, **kwargs):
        """
        Create an Auction
        Mandatory Fields:
            user_id, stuff_name, stuff_type, stuff_describe, start_price, create_time
        Options:
            place_id, stuff_image
        """
        if kwargs.get('user_id') is None:
            return dict(msg='Please create a auction with an user_id!'，
                        msg_cn='请传入正确的用户ID!'，
                        #error_code='',
                        warn='ok')
        if kwargs.get('stuff_name') is None:
            return dict(msg='Please create a auction with an stuff_name!'，
                        msg_cn='请传入要拍卖物品的名称!'，
                        #error_code='',
                        warn='ok')
        if kwargs.get('start_price') is None:
            return dict(msg='Please create a auction with an start_price!'，
                        msg_cn='请传入要拍卖物品的起拍价格!'，
                        #error_code='',
                        warn='ok')

        auction = Auction(user_id=kwargs.get('user_id'),
                            place_id=kwargs.get('place_id', ''),
                            stuff_name=kwargs.get('stuff_name'),
                            stuff_type=kwargs.get('stuff_type'),
                            stuff_describe=kwargs.get('stuff_describe'),
                            start_price=kwargs.get('start_price'),
                            )
        auction.save()
        return dict(msg='Success!',
                    #error_code='',
                    warn='none')

    def update_auction(cls, **kwargs):
        """
        Update an auction (it can only revisable when the stuff_status = 1)
        """








