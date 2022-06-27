from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class biller(models.Model):
    item_id=models.AutoField(primary_key=True, unique=True) #auto increment integer
    item_name=models.CharField(max_length=20, unique=True, null=False, blank=False)
    item_category=models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)])
    item_subcategory=models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.item_id)
