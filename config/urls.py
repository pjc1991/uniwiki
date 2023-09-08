"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView

from config import views

api_patterns = [
    path('common/', include('common.api_urls')),
    path('wiki/', include('wiki.api_urls')),
    path('auth/', include('dj_rest_auth.urls')),
]

urlpatterns = [
    path('', TemplateView.as_view(template_name='wiki/app.html'), name='index'),
    path('admin/', admin.site.urls),

    # API views
    path('api/', views.api_root, name='api-root'),
    path('api/', include(api_patterns)),
]
