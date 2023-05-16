from django.contrib.auth.models import User
from django.db import models


class Freelancers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    about_freelance = models.TextField(blank=True, verbose_name='О себе')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    cat = models.ForeignKey('Category',  verbose_name='Сфера', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name_category = models.CharField(max_length=30, db_index=True, verbose_name='Сфера')

    def __str__(self):
        return self.name_category

class Vacancies(models.Model):
    title_vacancy = models.CharField(max_length=30, verbose_name='Наименование вакансии')
    salary_vacancy = models.IntegerField(verbose_name='Зарплата')
    experience_vacancy = models.IntegerField(verbose_name='Опыт работы')
    skills_vacancy = models.CharField(max_length=100, verbose_name='Требуемые навыки')
    about_vacancy = models.TextField(verbose_name='О вакансии')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    cat = models.ForeignKey('Category', verbose_name='Сфера', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title_vacancy