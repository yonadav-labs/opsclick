from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings

from sitemaps import *
import views

admin.autodiscover()

sitemaps = {
    'blogs': BlogSitemap(),
    'static': StaticPagesSitemap(),
}

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns(
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    url("^admin/", include(admin.site.urls)),
)

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        url('^i18n/$', set_language, name='set_language'),
    ]

urlpatterns += [
    url('^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    url('^robots\.txt', include('robots.urls')),

    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    url(r'^accounts/', include('allauth.urls')),
    
    url(r"^platform", direct_to_template, {"template": "platform.html"}, name="platform"),
    url(r"^services", direct_to_template, {"template": "services.html"}, name="services"),
    url(r"^university", direct_to_template, {"template": "university.html"}, name="university"),
    url(r"^videos", direct_to_template, {"template": "videos.html"}, name="videos"),
    url(r"^news", direct_to_template, {"template": "news.html"}, name="news"),
    url(r"^learn-more", direct_to_template, {"template": "learn-more.html"}, name="learn-more"),
    url(r"^webinar_sign_up", views.webinar_sign_up, name="webinar_sign_up"),
    # url(r"^reference_sign_up", views.reference_sign_up, name="reference_sign_up"),

    url("^", include("mezzanine.urls")),
]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
