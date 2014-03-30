#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '19/03/2014'

from django.db import models
from apps.post.models import *


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn10 = models.CharField(blank=True, null=True)
    isbn13 = models.CharField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=False, null=False)
    origin_title = models.CharField(max_length=128, blank=True, null=True)
    alt_title = models.CharField(max_length=128, blank=True, null=True)
    sub_title = models.CharField(max_length=128, blank=True, null=True)
    book_image = models.CharField(max_length=32, blank=True, null=True)
    book_introduction = models.TextField(blank=True, null=True)
    book_recommended_text = models.TextField(blank=True, null=True)
    book_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rdb_book'

    def __str__(self):
        return '%s, %s, %s, %s' % (self.id, self.isbn10, self.isbn13, self.title)

    def create_book(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        return self

    def get_one_book(self, book_id):
        return self.objects.get(id=book_id)

    def update_book(self, book_id, **kwargs):
        self.objects.filter(id=book_id).update(**kwargs)

    def delete_post(self, book_id):
        self.objects.filter(id=book_id).update(book_status=1)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    origin_name = models.CharField(max_length=128, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    author_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rdb_author'


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    origin_name = models.CharField(max_length=64, blank=True, null=True)
    publisher_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rdb_publisher'


class BookAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.BigIntegerField(blank=False, null=False)
    author_id = models.BigIntegerField(blank=False, null=False)
    status = models.SmallIntegerField(blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'rdb_book_author'


class BookPublisher(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.BigIntegerField(blank=False, null=False)
    publisher_id = models.BigIntegerField(blank=False, null=False)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rdb_book_publisher'

