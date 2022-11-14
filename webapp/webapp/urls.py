from django.urls import path, include
from django.contrib import admin

from rest_framework.schemas import get_schema_view

from rest.routers import router
from ui import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("rest/", include(router.urls)),
    path('openapi', get_schema_view(), name='openapi-schema'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.HomeView.as_view(), name='home'),
]
