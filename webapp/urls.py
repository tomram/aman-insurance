from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('postQuery/', views.postQuery, name='contact'),
    path('confirmation/', views.submitConfirmation, name='submitConfirmation')
    ]