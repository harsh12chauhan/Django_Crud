"""
URL configuration for main project.

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
from django.urls import path

#importing userLists
from home.views import userLists
from about.views import moreDetails


urlpatterns = [
    path('admin/', admin.site.urls),
    # home app
    path('home/',userLists.as_view()),
    path('home/<int:id>/',userLists.as_view()),
    # about app
    path('about/',moreDetails.as_view()),
    path('about/<int:id>/',moreDetails.as_view()),
    
]
