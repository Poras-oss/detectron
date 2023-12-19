from django.db import models


# Create your models here.
class citizen_report(models.Model):
    incident_type = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    media = models.FileField(upload_to=None, max_length=100)

    name = models.CharField(default="", max_length=50)
    email = models.EmailField(default="", max_length=254)
    number = models.IntegerField(null=True)
    address = models.TextField(default="")

    def __str__(self):
        return self.name
