from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} from {self.year}'