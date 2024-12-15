from django.db import models

# Create your models here.
# Model for each baby tracked on the app
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Baby Allergies
    allergy = models.CharField(max_length=100)
    created_at_time = models.DateTimeField(auto_now_add=True)
    created_at_date = models.DateField(auto_now_add=True)

class BabyEvent(Baby):
    diaper_change = models.BooleanField(default=False)
    dirty_diaper = models.BooleanField(default=False)
    meal = models.CharField(max_length=100)
    sleep = models.DurationField()


    def __str__(self):
        # return self.name
        return f"Data: {self.name, self.dirty_diaper, self.diaper_change, self.meal, self.sleep} (Added at: {self.created_at_date, self.created_at_time})"