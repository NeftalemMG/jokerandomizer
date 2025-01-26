from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('thejokes.urls')),
    path('', include('thejokes.urls')),
]
