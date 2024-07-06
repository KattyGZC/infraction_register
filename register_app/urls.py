from django.urls import path

from .views import (PersonListView, PersonCreateView, PersonEditView, PersonDeleteView,
                    VehicleListView, VehicleCreateView, VehicleEditView, VehicleDeleteView,
                    OfficerListView, OfficerCreateView, OfficerEditView, OfficerDeleteView)

app_name = 'register_app'

urlpatterns = [
    path("person", PersonListView.as_view(), name="person_list"),
    path("person/create", PersonCreateView.as_view(), name="person_create"),
    path("person/edit/<int:pk>", PersonEditView.as_view(), name="person_edit"),
    path("person/delete/<int:pk>", PersonDeleteView.as_view(), name="person_delete"),

    path("vehicle", VehicleListView.as_view(), name="vehicle_list"),
    path("vehicle/create", VehicleCreateView.as_view(), name="vehicle_create"),
    path("vehicle/edit/<int:pk>", VehicleEditView.as_view(), name="vehicle_edit"),
    path("vehicle/delete/<int:pk>", VehicleDeleteView.as_view(), name="vehicle_delete"),

    path("officer", OfficerListView.as_view(), name="officer_list"),
    path("officer/create", OfficerCreateView.as_view(), name="officer_create"),
    path("officer/edit/<int:pk>", OfficerEditView.as_view(), name="officer_edit"),
    path("officer/delete/<int:pk>", OfficerDeleteView.as_view(), name="officer_delete"),
]
