from django.shortcuts import render
from django.views.generic import View

from ..models import Portfolio


class PortfolioView(View):
    template_name = "portfolio.html"

    def get(self, request):
        portfolios = Portfolio.objects.all()
        return render(request, self.template_name, {"portfolios": portfolios})
