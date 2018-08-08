"""tentechtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from shop.urls import router as shop_router
from tentechtest import routers

main_v1_api_router = routers.DefaultRouter()
main_v1_api_router.extend(shop_router)

main_v1_url_pattern = url(
    r'^v1/',
    include(
        main_v1_api_router.urls,
    )
)

urlpatterns = [
    main_v1_url_pattern,
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^v1/swagger/',
        get_swagger_view(title='Ten Tech Test API v1', patterns=[main_v1_url_pattern])
    ),
    url(
        r'v1/auth/', include('rest_auth.urls')
    )
]
