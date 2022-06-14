from django.shortcuts import render
from django.views.generic import View

from ..models import Feedback


class FeedbackView(View):
    template_name = "feedback.html"

    def get(self, request):
        feedbacks = Feedback.objects.all()
        return render(request, self.template_name, {"feedbacks": feedbacks})
