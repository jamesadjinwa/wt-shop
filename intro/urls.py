"""
Urls for landing page/Intro page
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$|^#contact$', views.intro, name="intro"),
    # url(r'^#contact$', views.contact, name="contact"),
]
