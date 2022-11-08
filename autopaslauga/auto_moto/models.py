from django.db import models
import uuid



# Create your models here.
class Car_model(models.Model):
    brand = models.CharField('brand', max_length=100, help_text = "Enter the car brand")
    car_model = models.CharField('model', max_length=100, help_text = "Enter the car model")


    def __str__(self) -> str:
        return f'{self.brand}, {self.car_model}' 

class Car(models.Model):
    plate_number = models.CharField("plate_number", max_length=50)
    car_model = models.ForeignKey(Car_model, verbose_name='car_model', on_delete=models.PROTECT)
    vin_code = models.CharField("vin_code", max_length=25, null=True, blank=True)
    client = models.CharField('client', max_length=200)

    def __str__(self) -> str:
        return f'{self.plate_number}, {self.vin_code}, {self.client}'


class Order(models.Model):
    date = models.DateField("date", max_length=20)
    car = models.ForeignKey(Car, verbose_name="car_id", on_delete=models.CASCADE)
    total = models.DecimalField("total", max_digits=18, decimal_places=2)

    ORDER_STATUS = (
        ('w', 'waiting for payment'),
        ('p', 'paid, car in warehouse'),
        ('d', 'delivered for client'),
    )
    status = models.CharField('status', max_length=1, choices=ORDER_STATUS, default='w')
    def __str__(self) -> str:
        return f'{self.date}, {self.total}'


class Service(models.Model):
    name = models.CharField("name", max_length=250)
    price = models.DecimalField("price", max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name}, {self.price}'

class Order_row(models.Model):
    service = models.ForeignKey("service", verbose_name="service", on_delete=models.CASCADE)
    order_id = models.ForeignKey("order", verbose_name="order", on_delete=models.CASCADE)
    quantity = models.DecimalField("quantity", max_digits=15, decimal_places=2)
    price = models.DecimalField("price", max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.quantity}, {self.price}'
