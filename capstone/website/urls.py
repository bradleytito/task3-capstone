from django.urls import path, include
from . import views


app_name = "website"
urlpatterns = [
    path('', views.user_login, name="user_login"),
    path('authenticatation/', views.authenticatation, name="authenticatation"),
    path('homepage/', views.homepage, name="homepage"),
    path('area_serviced/', views.area_serviced, name="area_serviced"),
    path('biography/', views.biography, name="biography"),
    path('endorsements/', views.endorsements, name="endorsements"),
    path('add_endorser/', views.add_endorser, name="add_endorser")
]