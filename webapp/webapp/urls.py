from django.urls import path, include
from django.contrib import admin
from rest.routers import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rest/", include(router.urls)),
]
