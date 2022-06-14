from django.urls import path

from .views import FeedbackView, PortfolioView, PriceView

urlpatterns = [
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
    path("price/", PriceView.as_view(), name="price"),
]
