from django.db import models

class students(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    studentid= models.IntegerField()
    def __str__(self):
        return self.firstname