from django.db import models

# Create your models here.
class Name(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ID(models.Model):
    id_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.id_number}'

class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.phone_number}, {self.email}'


class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state} {self.zip_code}'