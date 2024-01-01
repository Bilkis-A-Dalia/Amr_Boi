from django.db import models
from .constants import GENDER_TYPE
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user=models.OneToOneField(User, related_name='account',on_delete=models.CASCADE)
    balance=models.DecimalField(default=0, decimal_places=2, max_digits=12)
    birth_date=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_TYPE)

    def __str__(self) -> str:
        return self.user.username