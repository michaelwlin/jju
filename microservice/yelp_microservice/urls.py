from django.urls import path

from . import views

urlpatterns = [
    path("yelp", views.get_yelp, name="yelp")
]