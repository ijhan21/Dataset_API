from django.db import models

# Create your models here.
class Company_Class(models.Model):
    company_type = models.CharField(max_length = 30)

class Company(models.Model):
    company_code = models.CharField(max_length = 6, primary_key = True)
    company_name = models.CharField(max_length = 30)
    company_class = models.ForeignKey(Company_Class, on_delete=models.CASCADE)

class LabelType(models.Model):
    label_type = models.CharField(max_length = 30)

class Dataset(models.Model):
    company_code = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.CharField(max_length=30)
    close = models.IntegerField()
    open = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    vol = models.IntegerField()
    label_tpye = models.ForeignKey(LabelType, on_delete=models.CASCADE)