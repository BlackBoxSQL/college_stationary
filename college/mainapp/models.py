from django.db import models

# Create your models here.


class Company(models.Model):
    com_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=11)
    details = models.TextField()

    def __str__(self):
        return self.com_name


class Catagory(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name


class Rack(models.Model):
    rack_name = models.CharField(max_length=20)

    def __str__(self):
        return self.rack_name


class Products(models.Model):
    p_name = models.CharField(max_length=50)
    p_company = models.ForeignKey(Company, on_delete=models.PROTECT)
    asking_price = models.IntegerField()
    selling_price = models.IntegerField()
    buying_price = models.IntegerField()
    catagory = models.ForeignKey(Catagory, on_delete=models.PROTECT)
    rack_name = models.ForeignKey(Rack, on_delete=models.PROTECT)

    def __str__(self):
        return self.p_name


class Stock(models.Model):
    p_name = models.ForeignKey(Products, on_delete=models.PROTECT)
    qty = models.IntegerField()

    def __str__(self):
        return self.p_name, self.qty
