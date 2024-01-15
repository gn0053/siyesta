from django.db import models
from django.utils import timezone
# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.FloatField(default=0.0)
    unit_per_item = models.FloatField(default=1)
    description = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.item_name
    
    def unit_price(self):
        if(self.item_price > 0 and self.unit_per_item > 0):
            return self.item_price/self.unit_per_item
        else:
            return self.item_price