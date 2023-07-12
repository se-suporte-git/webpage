from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    pratica_esg = models.TextField()
    iniciativa_esg = models.TextField()
    # Outros campos ESG que você pode precisar

    def __str__(self):
        return self.nome
