from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from apps.main.urls import main_router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.registry.extend(main_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_v1/', include(router.urls)),
    path('', index),
]
