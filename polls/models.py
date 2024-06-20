from django.db import models

# Create your models here.
class Poll(models.Model):
    question=models.TextField()
    option_1=models.CharField(max_length=100)
    option_2=models.CharField(max_length=100)
    option_3=models.CharField(max_length=100)
    option_4=models.CharField(max_length=100)
    option_1_count=models.IntegerField(default=0)
    option_2_count=models.IntegerField(default=0)
    option_3_count=models.IntegerField(default=0)
    option_4_count=models.IntegerField(default=0)
    total=models.IntegerField(default=0)





    



