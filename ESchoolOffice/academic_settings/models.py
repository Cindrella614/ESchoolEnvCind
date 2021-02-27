from django.db import models

class Subject(models.Model):
    sub_name = models.CharField(max_length=60)

    def __str__(self):
        return self.sub_name
