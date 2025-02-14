from django.db import models

# Create your models here.
class Tour(models.Model): #一個類別一個表格
    #origin country, destination, nights, price
    origin_country = models.CharField(max_length=64) #這些都是欄位
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    #the string representation for the tour
    #紀錄物件的字串
    def __str__(self):
        return (f"ID:{self.id}: From:{self.origin_country} To:{self.destination_country}, {self.number_of_nights} nights costs ${self.price}")