from django.db import models

types = [('Site', 'Сайт'), ('Discord', 'Дискорд'), ('Guild', 'Гильдия'), ('Guide', 'Гайд'), ('Other', 'Другое')]
SITE = types[0][0]


class Link(models.Model):
    type = models.CharField(max_length=100, choices=types, default=SITE, verbose_name='Тип')
    url = models.URLField(max_length=500, verbose_name='Адрес')
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='links', verbose_name='Проект')

    def __str__(self):
        return f"{self.pk}. {self.type} - {self.project.name}"

    class Meta:
        db_table = "links"
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
