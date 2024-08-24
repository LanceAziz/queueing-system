from django.db import models
from django.contrib.auth.models import User


class Teller(User):
    num = models.IntegerField()
    type = models.CharField(max_length=45)

    def __str__(self):
        return str(self.teller_num)

class Client(models.Model):
    client_id = models.AutoField(primary_key=True, null=False)
    client_num = models.IntegerField()
    client_date = models.DateField(auto_now_add=True)
    client_time = models.TimeField(auto_now_add=True)
    client_type = models.CharField(max_length=45)
    client_audio = models.BooleanField(default=False)
    client_served = models.IntegerField(null=True, default=None)

    def __str__(self):
        return str(self.client_num)
