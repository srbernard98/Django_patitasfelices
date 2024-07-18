# forms.py
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'contraseña', 'dirección', 'teléfono', 'tipo_usuario']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
