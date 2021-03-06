"""job_interview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from job_list.views import home, signup
from Quiz import views
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('job.urls')),
    path('', home),
    path('signup', signup),
    path('quiz', include('Quiz.urls')),
    path('register/', views.register_view, name="register"),
]



if settings.DEBUG:
    urlpatterns += [
        re_path(r'^cv/(?P<path>.*)$', serve, {
                'document_root': settings.MEDIA_ROOT,
        }),
           ]
