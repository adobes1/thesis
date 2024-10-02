from enum import Enum

from django.db import models


class ReadState(Enum):
    PLANNED = 'Planned'
    READING = 'Reading'
    COMPLETED = 'Completed'
    DROPPED = 'Dropped'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[(state.name, state.value) for state in ReadState], default='Planned')

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Date: {self.publication_date}, Pages: {self.pages}, Status: {self.status.capitalize()} "
