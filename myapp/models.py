from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_joined = models.DateField(default=0)
    date_expired = models.DateField(default=0)

    def __str__(self):
        return self.name
