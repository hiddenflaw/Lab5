from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', include('myapp.urls')),
    path('', include('myapp.urls')),
]
