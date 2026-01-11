from django.db import models

class Summer(models.Model):
    city = models.CharField(max_length=40, blank=False)
    date = models.DateField(unique=True)
    description = models.CharField(max_length=400)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.city} - {self.date}'
