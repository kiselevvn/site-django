from django.db import models


class Feedback(models.Model):
    text = models.CharField(verbose_name="Отзыв",max_length=255)
    name = models.CharField(verbose_name="Имя",max_length=80)
    number = models.CharField(verbose_name="Номер телефона",max_length=12, blank=True)
    email = models.CharField(verbose_name="Электронная почта",max_length=60)
    date = models.DateTimeField(verbose_name="Дата отзыва",auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name='Отзывы'
        verbose_name_plural='Отзывы'
