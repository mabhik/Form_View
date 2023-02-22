from django.db import models

# Create your models here.

class college(models.Model):
    ids=models.BigIntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    no=models.IntegerField()

    def __str__(self):
        return self.cname

