from django.db import models


# Create your models here.
class Groceries(models.Model):
    id = models.AutoField(primary_key=True)
    fruits = models.CharField(max_length=50)
    vegetables = models.CharField(max_length=50)
    oil = models.CharField(max_length=70)

    class Meta:
        db_table = "mydata"
