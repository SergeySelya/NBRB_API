from django.db import models

class ExchangeRate(models.Model):
    cur_id = models.IntegerField()
    date = models.DateField()
    cur_abbreviation = models.CharField(max_length=100)
    cur_scale = models.IntegerField()
    cur_name = models.CharField(max_length=100)
    cur_officialRate = models.FloatField()

    def __str__(self):
        return self.Cur_Name
