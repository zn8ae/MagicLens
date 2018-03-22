from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^hello/', views.hello, name = 'hello'),
    url(r'^library/', views.library, name = 'library'),
    url(r'^logged/', views.logged, name = 'logged'),
    url(r'^predict/', views.predict, name = 'predict'),
    url(r'^history/', views.history, name = 'history'),
    url(r'^prediction/', views.prediction, name = 'prediction'),
]