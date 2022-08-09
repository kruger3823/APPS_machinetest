from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class mark(models.Model):
    date = models.DateField(max_length=200,null=True)
    register = models.CharField(max_length=200, null=True)
    #day = models.CharField(max_length=200,null=True)
    dis=(('malayalam','malayalam'),('english','english'),('hindi','hindi'),('maths','maths'))
    subjects = models.CharField(max_length=50,choices=dis)
    result = models.CharField(max_length=40,null=True)
    Grade=models.CharField(max_length=40,null=True)

