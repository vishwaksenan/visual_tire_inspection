"""tire_inspection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from admin_app import views as admin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',admin_view.tire_test_view,name='tire_testing_homepage'),
	path('ink/',admin_view.ink_test_view,name='ink_test_result'),
    path('twi/',admin_view.twi_test_view,name='scorch_test_result')
]
