from django.db import models


class MyApp(models.Model):
    app_name = models.CharField(max_length=100)
    points = models.IntegerField(default=1)
    img = models.ImageField(upload_to='img')
    