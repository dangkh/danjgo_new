from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.city_name


class Restaurant(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    res_name = models.CharField(max_length=200)
    res_address = models.CharField(max_length=200)
    res_description = models.CharField(max_length=400)
    def __str__(self):
        return self.res_name
