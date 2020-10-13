from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = ('titulo','subtitulo','cantidad','valor')

        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese título',
                }
            )
        }
    def clean_cantidad(self):
        cant = self.cleaned_data['cantidad']
        if cant > 20:
            raise forms.ValidationError('Cantidad máximo 20')

        return cant

