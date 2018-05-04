from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^hello/', views.hello, name = 'hello'),
    url(r'^map/', views.map, name = 'map'),
    url(r'^logged/', views.logged, name = 'logged'),
    url(r'^dashboard/', views.dashboard, name = 'dashboard'),
    url(r'^prediction/', views.prediction, name = 'prediction'),
    url(r'^predict/', views.predict, name = 'predict'),
]