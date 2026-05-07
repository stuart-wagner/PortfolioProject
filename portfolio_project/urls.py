"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.views.static import serve
from django.views.decorators.clickjacking import xframe_options_exempt
from django.urls import re_path

# Use an xframe_options_exempt wrapper for the serve view to allow embedding PDFs
@xframe_options_exempt
def serve_exempt(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root=document_root, show_indexes=show_indexes)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('favicon.ico', serve, {'document_root': settings.BASE_DIR, 'path': 'favicon.ico'}),
    re_path(r'^media/(?P<path>.*)$', serve_exempt, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    # In development, also serve static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)