from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from .views import LandingView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("content/", include("apps.content.urls")),
    path(
        "thanks/",
        TemplateView.as_view(template_name="thanks.html"),
        name="thanks",
    ),
    path("", LandingView.as_view(), name="home"),
]

urlpatterns = i18n_patterns(
    *urlpatterns,
    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar
    # pylint: disable=ungrouped-imports
    from django.conf.urls.static import static

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )
