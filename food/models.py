from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDnwVBHuYZsSc8j7YV82PckH30Tp4NaCRN1Q&s')
    
    def __str__(self):
        return self.item_name
    