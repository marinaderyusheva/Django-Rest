from rest_framework import serializers
from easyjob.models import *

# Сериализатор конвертирует пайтон в json файлы


# преобразовывает в формат JSON и обратно
class FreelancersSerializer(serializers.ModelSerializer):
    # создали скрытое поле, по дефолту пользователь, который сейчас на сайте
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Freelancers
        # fields = "__all__" - все поля
        fields = ("name", "surname", "age", "about_freelance", "cat", "user")


class VacanciesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Vacancies
        fields = "__all__"  # все поля





# class FreelancersModel:
    #  инициализатор
    # def __init__(self, name_freelancer, about_freelancer):
    #     # локальные атрибуты
    #     self.name_freelancer = name_freelancer
    #     self.about_freelancer = about_freelancer

# # преобразование верхнего класса в json
# class FreelancersSerializer(serializers.Serializer):
#     name_freelancer = serializers.CharField(max_length=100)
#     about_freelancer = serializers.CharField()

# кодирование FreelancersModel в json формат
# def encode():
#     model = FreelancersModel('Marina', 'about_freelancer: Marina')
#     # создаем объект сериализатора с метаклассом model, который вместо атрибутов
#     # класса FreelancersSerializer создает объект data
#     model_sr = FreelancersSerializer(model)
#     # представляет в виде словаря
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # словарь преобразовываем в JSON строку
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# декодирование из json в формат модели
# def decode():
#     # читаем json строку от клиента
#     stream = io.BytesIO(b'{"name_freelancer": "Marina", "about_freelancer":"Marina"}')
#     # формируем словарь с помощью JSONParser
#     data = JSONParser().parse(stream)
#     # преобразовываем набор данных data в объект сериализации
#     serializer = FreelancersSerializer(data=data)
#     # проверяем корректность принятых данных с помощью метода is_valid()
#     serializer.is_valid()
#     # после этого метода появится объект validated_data
#     print(serializer.validated_data)