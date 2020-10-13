from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Personaform."""

        model = Persona
        fields = (
            'first_name',
            'last_name',
            'departamento',
            'job',
            'avatar',
            'habilidades'
        )

        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(),
            'first_name': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese Nombre',
                }
            )
        }

