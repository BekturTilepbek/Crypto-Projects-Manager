from django.db import models

statuses = [('Active', 'Активный'), ('Finished', 'Завершен'), ('Abandoned', 'Забросил')]
ACTIVE = statuses[0][0]
INACTIVE = statuses[0][0]
priorities = [('Tier 1', 'Тир 1'), ('Tier 2', 'Тир 2'), ('Tier 3', 'Тир 3'), ('Antifomo', 'Антифомо')]
TIER_1 = priorities[0][0]
TIER_2 = priorities[1][0]
TIER_3 = priorities[2][0]
ANTIFOMO = priorities[3][0]


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=100, choices=statuses, default=ACTIVE, verbose_name='Статус')
    priority = models.CharField(max_length=100, choices=priorities, default=ANTIFOMO, verbose_name='Приоритет')
    info = models.TextField(null=True, blank=True, verbose_name='Инфа')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.pk}. {self.name} - {self.status}"

    class Meta:
        db_table = "projects"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
