from django.db import models

# Create your models here.


class AccountInfo(models.Model):
    account_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    profile_image = models.CharField(max_length=400)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "accountinfo"
