from django.db import models
from apps.alunos.models import Aluno
from apps.livros.models import Livro
from datetime import date

class Emprestimo(models.Model):
    aluno_id = models.ForeignKey(Aluno, verbose_name='Aluno', on_delete=models.CASCADE)
    livro_id = models.ForeignKey(Livro, verbose_name='Livro',on_delete=models.CASCADE)
    data_emprestimo = models.DateField(verbose_name='Data Empréstimo', auto_now_add=True)
    data_devolucao = models.DateField(blank=True, null=True, verbose_name='Data Devolução')
    data_prevista_devolucao = models.DateField(verbose_name='Previsão devolução')
    status = models.CharField(max_length=1, choices=[('E','Emprestado'), ('D','Devolvido')], default='E')

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'Emprestimo'
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['status']
        managed = True