from django.db import models


class Home(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='homepage')
    text = models.TextField('Содержимое', default=None)
    image = models.ImageField(
        'Главное изображение',
        default=None,
        upload_to='home'
    )
    image_second = models.ImageField(
        'Второе изображение',
        default=None,
        upload_to='home'
    )

    class Meta:
        verbose_name = 'home page'
        verbose_name_plural = 'home pages'


class Relevance(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='relevance'
    )
    text = models.TextField('Таблица аналитики', default=None)
    graph_up = models.ImageField(
        'Динамика уровня зарплат по годам',
        default=None,
        upload_to='relevance'
    )
    graph_middle = models.ImageField(
        'Динамика количества вакансий по годам',
        default=None,
        upload_to='relevance'
    )
    graph_down = models.ImageField(
        'Динамика количества вакансий по годам для профессии',
        default=None,
        upload_to='relevance'
    )
    result = models.TextField(
        'Результат анализа по странице',
        default=None
    )

    class Meta:
        verbose_name = 'relevance page'
        verbose_name_plural = 'relevance pages'


class Geography(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geography'
    )
    table_salary = models.TextField('Таблица о зарплате', default=None)
    table_percent = models.TextField('Таблица о проценте', default=None)
    graph = models.ImageField(
        'График доли вакансий по городам',
        default=None,
        upload_to='geography'
    )
    result = models.TextField(
        'Результат анализа по странице',
        default=None
    )

    class Meta:
        verbose_name = 'geography page'
        verbose_name_plural = 'geography pages'


class Skills(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    text = models.TextField('Содержимое', default=None)
    result = models.TextField(
        'Результат анализа по странице',
        default=None
    )

    class Meta:
        verbose_name = 'skills page'
        verbose_name_plural = 'skills pages'


class LastVacancies(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='last_vacancies'
    )

    class Meta:
        verbose_name = 'vacancy page'
        verbose_name_plural = 'vacancies pages'
