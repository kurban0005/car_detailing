from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    '''Модель заказа.'''
    name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True)
    car_model = models.CharField(max_length=30)
    question = models.TextField(max_length=500)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Возвращает строковое представление модели.'''
        return f' {self.phone_number} | {self.name[:15]} | {self.car_model[:15]}'
