from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=30)
    year = models.IntegerField('Год')
    content = models.CharField('Содержимое', max_length=255)

    def __str__(self):
        return f"{self.title} - {self.author} {self.year}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ManyToManyField(Book)
    is_active = models.BooleanField('Статус', null=True)

    def __str__(self):
        return f"Order №{self.id}"


class Mail(models.Model):
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    adress = models.CharField('Адрес', max_length=50)
    index = models.IntegerField('Почтовый индекс')

    def __str__(self):
        return f"{self.order} - {self.adress} {self.index}"
