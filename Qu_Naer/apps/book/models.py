
__author__ = 'gong'

from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn10 = models.CharField(blank=True, null=True)
    isbn13 = models.CharField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=False, null=False)
    origin_title = models.CharField(max_length=128, blank=True, null=True)
    alt_title = models.CharField(max_length=128, blank=True, null=True)
    sub_title = models.CharField(max_length=128, blank=True, null=True)
    book_image = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rdb_book'


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    origin_name = models.CharField(max_length=128, blank=True, null=True)
    introduction = models.CharField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rdb_author'


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    origin_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rdb_publisher'


class BookAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.BigIntegerField(blank=False, null=False)
    author = models.BigIntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'rdb_book_author'


class BookPublisher(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.BigIntegerField(blank=False, null=False)
    publisher = models.BigIntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'rdb_book_publisher'

