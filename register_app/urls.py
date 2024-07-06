from django.urls import path

from .views import (PersonListView, PersonCreateView, 
                    VehicleListView, VehicleCreateView, 
                    OfficerListView, OfficerCreateView)

app_name = 'register_app'

urlpatterns = [
    path("person", PersonListView.as_view(), name="person_list"),
    path("person/create", PersonCreateView.as_view(), name="person_create"),
    path("vehicle", VehicleListView.as_view(), name="vehicle_list"),
    path("vehicle/create", VehicleCreateView.as_view(), name="vehicle_create"),
    path("officer", OfficerListView.as_view(), name="officer_list"),
    path("officer/create", OfficerCreateView.as_view(), name="officer_create"),
]
