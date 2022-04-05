from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User

class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class GraphiCards(models.Model):
    name = models.CharField(max_length=30)
    Reference = models.CharField(default='145',max_length=30)
    image = models.FileField(upload_to='authapp/static/authapp/images')
    Quantity = models.IntegerField()
    price = models.FloatField()
#    def save(self):
#        self.file_name = self.Rep.split('//')[:-1]
#        super().save(self)
    def __str__(self):
        return self.name
    def update_quntiy(self):
        self.Quantity = self.Quantity-1
        return self.Quantity







