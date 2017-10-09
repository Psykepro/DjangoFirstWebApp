"""muypicky URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import (
    LoginView,PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^u/', include('profiles.urls', namespace='profile')),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name = 'contact.html'), name='contact'), #(?P<id>\d+)/ regex for id
    url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]