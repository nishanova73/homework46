from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'new'), ('in_progress', 'in progress'),  ('done', 'done')]

class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='description')
    status = models.CharField(max_length=50, null=False, blank=False, default='new', verbose_name='status')
    detailed_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='detailed_description')
    create_until = models.DateField(null=True, blank=True, verbose_name='Create_until')
    status = models.CharField(max_length=15, default='new', choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status}"

    class Meta:
        db_table = 'Tasks'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'