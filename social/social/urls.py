"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from socialapp import views
from django.conf.urls.static import  static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.reg),
    path('login/',views.log),
    path('friends/',views.fnds),
    path('findf/',views.findf),
    path('findl',views.findf),
    path('profile/',views.prf),
    path('rqst/',views.req),
    path('flist/',views.flist),
    path('freq/',views.frqst),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
