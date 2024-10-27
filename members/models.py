from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.PositiveSmallIntegerField()
    updated = models.DateTimeField( auto_now = True )  
    """I want now as datetime default """   
    
    # def __str__(self) -> str:
    #     return f"{self.first_name} {self.last_name} {self.salary} {self.updated}"