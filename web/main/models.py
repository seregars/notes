from django.db import models


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    task = models.TextField('Содержание')

    def __str__(self):
        return self.title
