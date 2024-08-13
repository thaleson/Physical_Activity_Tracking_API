from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    """
    Modelo que representa um exercício.

    Attributes:
        name (str): Nome do exercício.
        description (str): Descrição detalhada do exercício.
        duration (timedelta): Duração do exercício.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()  # Duração do exercício

    def __str__(self):
        """
        Retorna a representação em string do exercício.

        Returns:
            str: Nome do exercício.
        """
        return self.name


class Goal(models.Model):
    """
    Modelo que representa uma meta de um usuário.

    Attributes:
        user (User): Usuário associado à meta.
        name (str): Nome da meta.
        target (float): Meta numérica a ser alcançada.
        achieved (float): Progresso atual em relação à meta.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target = models.FloatField()  # Meta numérica
    achieved = models.FloatField(default=0)  # Progresso

    def __str__(self):
        """
        Retorna a representação em string da meta.

        Returns:
            str: Nome da meta.
        """
        return self.name


class Workout(models.Model):
    """
    Modelo que representa um treino realizado por um usuário.

    Attributes:
        user (User): Usuário que realizou o treino.
        exercise (Exercise): Exercício realizado.
        date (date): Data em que o treino foi realizado.
        duration (timedelta): Duração do treino.
        notes (str): Notas adicionais sobre o treino.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    notes = models.TextField(blank=True)

    def __str__(self):
        """
        Retorna a representação em string do treino.

        Returns:
            str: Representação em string do treino, incluindo usuário, exercício e data.
        """
        return f'{self.user} - {self.exercise} - {self.date}'
