from django.shortcuts import render
from django.views.generic import View

from ..models import PriceService


class PriceView(View):
    template_name = "price.html"

    def get(self, request):
        prices = PriceService.objects.all()
        return render(request, self.template_name, {"prices": prices})
