from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Person, Vehicle, Officers, Infraction
from .serializers import InfractionSerializer, TokenObtainSerializer


class PersonListView(ListView):
    model = Person
    template_name = 'register_app/list.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Personas'
        context['url_create'] = reverse('register_app:person_create')
        context['items_with_urls'] = [
            {
                'obj': obj,
                'url_edit': reverse('register_app:person_edit', kwargs={'pk': obj.pk}),
                'url_delete': reverse('register_app:person_delete', kwargs={'pk': obj.pk}),
                'url_detail': reverse('register_app:person_detail', kwargs={'pk': obj.pk}),
            }
            for obj in self.object_list
        ]
        return context


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Vehículos'
        context['url_create'] = reverse('register_app:vehicle_create')
        context['items_with_urls'] = [
            {
                'obj': obj,
                'url_edit': reverse('register_app:vehicle_edit', kwargs={'pk': obj.pk}),
                'url_delete': reverse('register_app:vehicle_delete', kwargs={'pk': obj.pk}),
                'url_detail': reverse('register_app:vehicle_detail', kwargs={'pk': obj.pk}),
            }
            for obj in self.object_list
        ]
        return context


class OfficerListView(ListView):
    model = Officers
    template_name = 'register_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Oficiales'
        context['url_create'] = reverse('register_app:officer_create')
        context['items_with_urls'] = [
            {
                'obj': obj,
                'url_edit': reverse('register_app:officer_edit', kwargs={'pk': obj.pk}),
                'url_delete': reverse('register_app:officer_delete', kwargs={'pk': obj.pk}),
                'url_detail': reverse('register_app:officer_detail', kwargs={'pk': obj.pk}),
            }
            for obj in self.object_list
        ]
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
        context["action"] = 'Crear'
        return context


class VehicleCreateView(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'register_app/form.html'
    success_url = reverse_lazy('register_app:vehicle_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo registro de vehículo'
        context['action'] = 'Crear'
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
        context['action'] = 'Crear'
        context["url"] = reverse('register_app:officer_list')
        return context


class PersonEditView(UpdateView):
    model = Person
    fields = '__all__'
    template_name = "register_app/form.html"
    success_url = reverse_lazy('register_app:person_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edición de registro'
        context["action"] = 'Guardar'
        context["url"] = reverse('register_app:person_list')
        return context


class VehicleEditView(UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name = "register_app/form.html"
    success_url = reverse_lazy('register_app:vehicle_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edición de registro'
        context["action"] = 'Guardar'
        context["url"] = reverse('register_app:vehicle_list')
        return context


class OfficerEditView(UpdateView):
    model = Officers
    fields = '__all__'
    template_name = "register_app/form.html"
    success_url = reverse_lazy('register_app:officer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edición de registro'
        context["action"] = 'Guardar'
        context["url"] = reverse('register_app:officer_list')
        return context


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'register_app/delete_confirm_form.html'
    success_url = reverse_lazy('register_app:person_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = reverse('register_app:person_list')
        return context


class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'register_app/delete_confirm_form.html'
    success_url = reverse_lazy('register_app:vehicle_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = reverse('register_app:vehicle_list')
        return context


class OfficerDeleteView(DeleteView):
    model = Officers
    template_name = 'register_app/delete_confirm_form.html'
    success_url = reverse_lazy('register_app:officer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = reverse('register_app:officer_list')
        return context


class PersonDetailView(DetailView):
    model = Person
    template_name = 'register_app/detail.html'
    success_url = reverse_lazy('register_app:person_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = reverse('register_app:person_list')
        context['url_edit'] = reverse(
            'register_app:person_edit', kwargs={'pk': self.object.pk})
        context['url_delete'] = reverse(
            'register_app:person_delete', kwargs={'pk': self.object.pk})
        context['fields'] = [(field.verbose_name, field.value_from_object(
            self.object)) for field in self.object._meta.fields]
        return context


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'register_app/detail.html'
    success_url = reverse_lazy('register_app:vehicle_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = reverse('register_app:vehicle_list')
        context['url_edit'] = reverse(
            'register_app:vehicle_edit', kwargs={'pk': self.object.pk})
        context['url_delete'] = reverse(
            'register_app:vehicle_delete', kwargs={'pk': self.object.pk})
        fields = []
        for field in self.object._meta.fields:
            value = getattr(self.object, field.name)
            if field.is_relation:
                value = str(value)
            fields.append((field.verbose_name, value))

        context['fields'] = fields
        return context


class OfficerDetailView(DetailView):
    model = Officers
    template_name = 'register_app/detail.html'
    success_url = reverse_lazy('register_app:officer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = reverse('register_app:officer_list')
        context['url_edit'] = reverse(
            'register_app:officer_edit', kwargs={'pk': self.object.pk})
        context['url_delete'] = reverse(
            'register_app:officer_delete', kwargs={'pk': self.object.pk})
        context['fields'] = [(field.verbose_name, field.value_from_object(
            self.object)) for field in self.object._meta.fields]
        return context


OK = status.HTTP_200_OK
NOT_FOUND = status.HTTP_404_NOT_FOUND
SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR


class TokenObtainView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TokenObtainSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                'status': 'success',
                'data': serializer.validated_data,
            }, status=OK)
        return Response({
            'status': 'error',
            'errors': serializer.errors,
        }, status=NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cargar_infraccion(request):
    """
    create a new infraction.
    """
    if request.method == 'POST':

        if not request.data.get('patente'):
            response_data = {
                'status': NOT_FOUND,
                'message': "El parámetro 'patente' es obligatorio."
            }
            return Response(response_data, status=NOT_FOUND)

        serializer = InfractionSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
                response_data = {
                    'status': OK,
                    'object': serializer.data,
                    'msj': 'Infracción registrada con éxito.'
                }
                return Response(response_data, status=OK)

            except Exception as e:
                response_data = {
                    'status': SERVER_ERROR,
                    'msj': 'Ocurrió un error inesperado.',
                    'errors': str(e)
                }
                return Response(response_data, status=SERVER_ERROR)
        else:
            response_data = {
                'status': NOT_FOUND,
                'message': 'Errores de validación.',
                'errors': serializer.errors
            }
            return Response(response_data, status=NOT_FOUND)


@api_view(['GET'])
def generar_informe(request):
    if request.method == 'GET':
        email = request.query_params.get('email')
        infracctions = Infraction.objects.filter(
            vehicle__person__email=email).order_by('timestamp')
        if infracctions.exists():
            serializer = InfractionSerializer(infracctions, many=True)
            response_data = {
                'status': OK,
                'objects': serializer.data,
                'msj': 'Infracciones encontradas.'
            }

        else:
            response_data = {
                'status': NOT_FOUND,
                'objects': [],
                'msj': 'No se encontraron infracciones.'
            }

        return Response(response_data)
