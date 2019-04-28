"""aiarena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from aiarena.core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('rules', TemplateView.as_view(template_name='rules.html'), name='rules'),
    path('api/', include('aiarena.api.urls')),
    path('ranking/', core_views.Ranking.as_view(), name='ranking'),
    path('results/', core_views.Results.as_view(), name='results'),
    path('botupload/', core_views.BotUpload.as_view(), name='botupload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # https://stackoverflow.com/questions/5517950/django-media-url-and-media-root