"""
Urls for landing page/Intro page
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.intro, name="intro"),
    # url(r'^#contact$', views.contact, name="contact"),
    url(r'^privacy-policy$', views.privacy_policy, name="privacy_policy"),
]
