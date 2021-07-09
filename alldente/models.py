from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class table(models.Model):
    table_number = models.IntegerField(default=1, unique=True)
    table_chairs = models.IntegerField(default=1,)

    def __str__(self):
        return f'Table ( {self.table_number} ), chairs: {self.table_chairs}'
