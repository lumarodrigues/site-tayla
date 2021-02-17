from django.forms import ModelForm

from projeto.base.models import Formulario


class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'email', 'mensagem']
