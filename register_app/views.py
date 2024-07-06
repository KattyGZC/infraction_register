from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Person, Vehicle, Officers, Infraction

class PersonListView(ListView):
    model = Person
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Personas'
        context['url_create'] = reverse('register_app:person_create')
        return context
    

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Vehículos'
        context['url_create'] = reverse('register_app:vehicle_create')
        return context


class OfficerListView(ListView):
    model = Officers
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Oficiales'
        context['url_create'] = reverse('register_app:officer_create')
        return context  

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'register_app/form.html'
    success_url = reverse_lazy('register_app:person_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo registro de Persona'
        context["url"] = reverse('register_app:person_list')
        return context 


class VehicleCreateView(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'register_app/form.html'
    success_url = reverse_lazy('register_app:vehicle_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo registro de vehículo'
        context["url"] = reverse('register_app:vehicle_list')
        return context 
    

class OfficerCreateView(CreateView):
    model = Officers
    fields = '__all__'
    template_name = 'register_app/form.html'
    success_url = reverse_lazy('register_app:officer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo registro de Oficial'
        context["url"] = reverse('register_app:officer_list')
        return context 