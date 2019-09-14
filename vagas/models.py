from django.db import models


class Vaga(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.titulo}] {self.descricao[:42]}..."

    class Meta:
        verbose_name = "vaga"
        verbose_name_plural = "vagas"
        ordering = ["-created"]


class Requisito(models.Model):
    vaga = models.ForeignKey("Vaga", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    obrigatorio = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.vaga.titulo}] {self.descricao}"


class Beneficio(models.Model):
    vaga = models.ForeignKey("Vaga", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.vaga.titulo}] {self.descricao}"