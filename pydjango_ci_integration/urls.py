"""pydjango_ci_integration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
"""
from django.conf.urls import url, include
from django.contrib import admin

from tasks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('tasks.urls'))
]

handler404 = views.Custom404.as_view()
handler500 = views.Custom500.as_view()
"""
#---
"""pydjango_ci_integration URL Configuration

For more details, see:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include, re_path

from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]

# Custom error handlers
handler404 = views.Custom404.as_view()
handler500 = views.Custom500.as_view()
