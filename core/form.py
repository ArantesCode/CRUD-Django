from django.forms import ModelForm
from .models import Alunos

class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'sobrenome', 'idade', 'email', 'turma']