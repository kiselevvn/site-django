# from apps.content.forms import MessageForm
# from apps.content.models import (
# )
from django.shortcuts import render
from django.views.generic import View


class LandingView(View):
    """
    Лэндиннг сайта
    """

    template_name = "home.html"



    def get(self, request):
        """
        Обработка GET запроса
        """

        return render(request=request, template_name=self.template_name, context={})


