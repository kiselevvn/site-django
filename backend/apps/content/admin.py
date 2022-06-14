from django.contrib import admin

from .models import Feedback, Portfolio, PriceService


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    # list_display = (
    #     # "filed",
    # )
    # list_filter = (
    #     # "filed",
    # )
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    # list_display = (
    #     # "filed",
    # )
    # list_filter = (
    #     # "filed",
    # )
    pass


@admin.register(PriceService)
class PriceServiceAdmin(admin.ModelAdmin):
    # list_display = (
    #     # "filed",
    # )
    # list_filter = (
    #     # "filed",
    # )

    pass
