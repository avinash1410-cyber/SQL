from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=60,null=True,blank=True)

    def __str__(self):
        return self.name