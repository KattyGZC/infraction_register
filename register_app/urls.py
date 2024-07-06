from django.urls import path

from . import views 

app_name = 'register_app'

urlpatterns = [
    path("person", views.PersonListView.as_view(), name="person_list"),
    path("person/create", views.PersonCreateView.as_view(), name="person_create"),
    path("person/edit/<int:pk>", views.PersonEditView.as_view(), name="person_edit"),
    path("person/delete/<int:pk>", views.PersonDeleteView.as_view(), name="person_delete"),
    path("person/<int:pk>", views.PersonDetailView.as_view(), name="person_detail"),

    path("vehicle", views.VehicleListView.as_view(), name="vehicle_list"),
    path("vehicle/create", views.VehicleCreateView.as_view(), name="vehicle_create"),
    path("vehicle/edit/<int:pk>", views.VehicleEditView.as_view(), name="vehicle_edit"),
    path("vehicle/delete/<int:pk>", views.VehicleDeleteView.as_view(), name="vehicle_delete"),
    path("vehicle/<int:pk>", views.VehicleDetailView.as_view(), name="vehicle_detail"),

    path("officer", views.OfficerListView.as_view(), name="officer_list"),
    path("officer/create", views.OfficerCreateView.as_view(), name="officer_create"),
    path("officer/edit/<int:pk>", views.OfficerEditView.as_view(), name="officer_edit"),
    path("officer/delete/<int:pk>", views.OfficerDeleteView.as_view(), name="officer_delete"),
    path("officer/<int:pk>", views.OfficerDetailView.as_view(), name="officer_detail"),

    path('api/cargar-infraccion', views.cargar_infraccion, name='cargar_infraccion'),
    path('api/generar-informe', views.generar_informe, name='generar_informe'),
]
