from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    text = models.CharField(max_length=600, blank=False)
    checkbox = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.text}'
