from django.shortcuts import render
from django.views.generic import View

from ..forms import FeedbackForm
from ..models import Feedback


class FeedbackView(View):
    template_name = "feedback.html"

    def get(self, request):
        """
        Обработка GET запроса
        """
        form = FeedbackForm()
        return render(request, template_name=self.template_name, context={"form":form})


    def post(self, request):
        """
        Обработка POST запроса
        """
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save()
            return render(request, template_name=self.template_name, context={"form":form, "instance":form_instance})
        return render(request, template_name=self.template_name, context={"form":form})
