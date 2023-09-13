"""
URL configuration for PKS project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flim.urls')),
    path('operator/', include('flim.urls')),
    path('bus_details/', include('flim.urls')),
    path('route_details/', include('flim.urls')),
    path('bus_schedule/', include('flim.urls')),
    path('book/', include('flim.urls')),
    path('pay/', include('flim.urls')),
    path('reser/', include('flim.urls')),
    path('review/', include('flim.urls')),
    path('', include('flim.urls')),

]
