from django import forms
from .models import Veiculo, Registro

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['tipo', 'modelo', 'cor', 'placa']
        
class RegistroForm(forms.ModelForm):
    veiculo = forms.ModelChoiceField(queryset=None)
    
    class Meta:
        model = Registro
        fields = ['veiculo', 'data_hora']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.filter(usuario=user)