from django.db import models


class Book(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=30)
    year = models.IntegerField('Год')
    content = models.CharField('Содержимое', max_length=255)

    def __str__(self):
        return f"{self.title} - {self.author} {self.year}"
