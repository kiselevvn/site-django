from django.forms import BooleanField, ModelForm

from .models import Feedback


class FeedbackForm(ModelForm):

    privacy = BooleanField(required=True)

    class Meta:
        model = Feedback
        fields = [
            "text", "name", "number", "email",
        ]
