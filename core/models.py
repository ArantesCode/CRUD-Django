from django.db import models



class Turma(models.Model):
    serie = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Turmas"

    def __str__(self):
        return self.serie


class Alunos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=120, null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    turma = models.ForeignKey(Turma, on_delete= models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Alunos"

    def __str__(self):
       return self.nome
