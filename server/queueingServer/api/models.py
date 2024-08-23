from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Voice(models.Model):
    voice_id = models.AutoField(primary_key=True, null=False)
    voice_name = models.CharField(max_length=45)
    voice_file = models.CharField(max_length=300)

    def __str__(self):
        return self.voice_name

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
    client_teller_id = models.ForeignKey(Teller, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.client_num)
