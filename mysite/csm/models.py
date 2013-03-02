from django.db import models

class Data(models.Model):
  l1 = models.FloatField()
  l2 = models.FloatField()
  l3 = models.FloatField()
  sum = models.FloatField()
  pub_date = models.DateTimeField('read time')