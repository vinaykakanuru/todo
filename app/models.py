from django.db import models

# Create your models here.


class ToDo(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ToDo'
        verbose_name = 'ToDo'
        ordering = ['-added_date']

    def __str__(self):
        return self.name
