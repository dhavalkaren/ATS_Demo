from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
