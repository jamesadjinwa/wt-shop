"""
Urls for landing page/Intro page
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.intro, name="intro"),
    url(r'^$', views.contact, name="contact")
]
