from django.db import models

class ShapeEntity(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=200)
  width = models.IntegerField()
  height = models.IntegerField()
  depth = models.IntegerField()
  creation_date = models.DateTimeField(auto_now_add=True)