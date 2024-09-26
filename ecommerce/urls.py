"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView #  URL redirects.
from decouple import config
from django.conf.urls.static import static # static and media file serving
from drf_yasg import openapi # metadata for the API, such as title
from django.urls import re_path as url #  Allo the use of regular expressions in URLs
from rest_framework import permissions # permission classes for API access control
from drf_yasg.views import get_schema_view # rendering api documentation (Swager/Redoc)

public_apis = [
    url(r"^api/account/", include("orders.urls")),
    url(r"^api/order/", include("orders.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title=config("API_TITLE"),
        default_version=config("API_VERSION"),
        description="APIs for Ordering Application",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),# No authentication is required
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("djoser.urls.jwt")), # for integrate JWT authentication using the djoser for login
    path(
        "developer/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "developer/doc",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
# appending apis to urlpatterns
urlpatterns += public_apis
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin Interface Customization
admin.site.site_header = config("ADMIN_SITE_HEADER")
admin.site.site_title = config("ADMIN_SITE_TITLE")
admin.site.index_title = config("ADMIN_SITE_INDEX_TITLE")