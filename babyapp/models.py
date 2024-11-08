from django.db import models

# Create your models here.
# Model for each baby tracked on the app
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Baby Allergies
    allergy = models.CharField(max_length=100)

    def __str__(self):
        return self.name