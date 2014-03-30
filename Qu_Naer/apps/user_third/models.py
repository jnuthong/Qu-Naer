from django.db import models

class UserThird(models.Model):
    third_key = models.CharField(max_length=128, null=True)
    user_id = models.BigIntegerField(max_length=32, primary_key=True)
    access_token = models.CharField(max_length=128, null=True)
    refresh_token = models.CharField(max_length=256, null=True)
    expire_time = models.DateTimeField(null=True)
    create_time = models.DateTimeField(null=True)
    modify_time = models.DateTimeField(null=True)
    third_type = models.IntegerField(null=True)
    flag = models.IntegerField(null=True)
    third_name = models.CharField(max_length=128, null=True)
    status = models.SmallIntegerField(max_length=2, null=True)

    class Meta:
        db_table = 'rdb_user_third'
        index_together = [
            ["third_key"],
            ["access_token"],
            ["user_id"],
        ]