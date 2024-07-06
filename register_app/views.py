from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Person, Vehicle, Officers, Infraction

class PersonListView(ListView):
    model = Person
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Personas'
        return context
    

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Vehículos'
        return context


class OfficerListView(ListView):
    model = Officers
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Oficiales'
        return context    
