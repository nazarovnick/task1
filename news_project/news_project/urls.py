"""news_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news_app.views import index_page, NewsViewSet, GenerateExcelView
from news_project import settings
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'news', NewsViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('api/', include(router.urls)),
    path('api/export/news', GenerateExcelView.as_view(), name = 'export_xlsx'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)