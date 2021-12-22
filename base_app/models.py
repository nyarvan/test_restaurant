from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator

class CategoryDish(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    is_visibility = models.BooleanField(default=True)
    position = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ("position", )

    def __str__(self):
        return f"{self.name}: {self.position}"


class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join("images/dishes", filename)

    category = models.ForeignKey(CategoryDish, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    ingredients = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=get_file_name)
    description = models.TextField(blank=True)
    dish_order = models.PositiveIntegerField()
    is_visibility = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    class Meta:
        ordering = ("dish_order",)

    def __str__(self):
        return f"{self.title}: {self.price}"

class Reservation(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')

    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[mobile_regex])
    date = models.DateField()
    time = models.TimeField()
    count_people = models.PositiveIntegerField()
    message = models.TextField(max_length=500, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-time',)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}'

class Event(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join("images/dishes", filename)

    title = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=get_file_name)
    description = models.TextField(max_length=500)
    position = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.title}'

