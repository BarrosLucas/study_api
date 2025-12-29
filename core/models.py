from django.db import models


class Discipline(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class StudySession(models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField()
    total_time = models.DurationField()
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        related_name='study_sessions'
    )

    def __str__(self):
        return f'{self.discipline.name} - {self.total_time}'
