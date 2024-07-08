from django.db import models

class Person(models.Model):
    name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Email', max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class Vehicle(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Persona')
    patent = models.CharField('Placa de patente', max_length=15, unique=True)
    brand = models.CharField('Marca', max_length=100)
    color = models.CharField('Color', max_length=50)

    def __str__(self) -> str:
        return f'PLACA: {self.patent} - {self.person.name}'

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'



class Officers(models.Model):
    name = models.CharField('Nombre', max_length=100)
    nui = models.IntegerField('Nro. Único Identificatorio', unique=True)

    def __str__(self) -> str:
        return f'NUI: {self.nui} - {self.name}'
    
    @property
    def is_authenticated(self):
        return True
    
    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales'


class Infraction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Vehículo')
    timestamp = models.DateTimeField('Fecha y hora')
    comment = models.CharField('Comentarios', max_length=100)

    def __str__(self) -> str:
        return f'Infracción {self.vehicle}'

    class Meta:
        verbose_name = 'Infracción'
        verbose_name_plural = 'Infracciónes'