from django.db import models


class PriceService(models.Model):
    service_name = models.CharField(verbose_name="Название услуги",max_length=60)
    price = models.CharField(verbose_name="Цена",max_length= 40)
    time_completion = models.CharField(verbose_name="Время исполнения",max_length= 40)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name='Цена услуг'
        verbose_name_plural='Цены услуг'
