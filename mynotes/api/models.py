from django.db import models

# Create your models here.
class Note(models.Model):
    body=models.TextField(null=True, blank=True) #blank to ensure that w can submit a form with null data in this field
    updated=models.DateTimeField(auto_now=True) #each timenote is saved, the stamp is written
    created=models.DateTimeField(auto_now_add=True) #time of creation

    def __str__(self):
        return self.body[0:50]