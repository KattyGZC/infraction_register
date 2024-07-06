from django.urls import path

from .views import PersonListView

app_name = 'register_app'

urlpatterns = [
    path("person", PersonListView.as_view(), name="person_list"),
    path("vehicle", PersonListView.as_view(), name="vehicle_list"),
    path("officer", PersonListView.as_view(), name="officer_list"),
]