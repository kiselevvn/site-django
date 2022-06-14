from django.db import models


class Portfolio(models.Model):
    project_name = models.CharField(verbose_name="Название проекта",max_length=60)
    customer = models.CharField(verbose_name="Заказчик",max_length=40)
    time_completion = models.CharField(verbose_name="Время завершения",max_length=40)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name='Портфолио'
        verbose_name_plural='Портфолио'
