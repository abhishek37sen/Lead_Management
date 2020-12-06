from django.db import models

# Create your models here.
class source_list(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=200)
    contact_person_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    person_number = models.IntegerField()
    current_stage = models.BooleanField(default=1)
    objects = models.Manager()
    def __str__(self):
        return self.source

class followup_history(models.Model):
    source_id=models.ForeignKey(source_list,on_delete=models.CASCADE,default=1)
    date_of_follow_up = models.DateField()
    response = models.CharField(max_length=100)
    medium = models.CharField(max_length=200)
    objects = models.Manager()