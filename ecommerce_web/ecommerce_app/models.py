from django.db import models

# Create your models here.


class AccountInfo(models.Model):
    userid = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=20)
    profileImage = models.CharField(max_length=400)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "accountinfo"
