from rest_framework import generics
from rest_framework.permissions import *
from easyjob.models import *
from easyjob.permissions import *
from easyjob.serializers import *


# возвращает список по GET и добавляет по POST
class FreelancersApiList(generics.ListCreateAPIView):
    queryset = Freelancers.objects.all()
    serializer_class = FreelancersSerializer
    # ограничение доступа
    permission_classes = (IsAuthenticatedOrReadOnly, )

# выполняем PUT(изменяем записи в БД) запросы на адрес freelancerslist/<int:pk>
class FreelancersApiUpdate(generics.UpdateAPIView):
    queryset = Freelancers.objects.all()
    serializer_class = FreelancersSerializer
    permission_classes = (IsOwnerOrReadOnly, )

# CRUD - create, read, update, delete
class FreelancersAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Freelancers.objects.all()
    serializer_class = FreelancersSerializer
    permission_classes = (IsAdminOrReadOnly, )

# возвращает список по GET и добавляет по POST
class VacanciesApiList(generics.ListCreateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    # ограничение доступа
    permission_classes = (IsAuthenticatedOrReadOnly, )

# выполняем PUT(изменяем записи в БД) запросы на адрес freelancerslist/<int:pk>
class VacanciesApiUpdate(generics.UpdateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = (IsOwnerOrReadOnly, )

# CRUD - create, read, update, delete
class VacanciesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = (IsAdminOrReadOnly, )


# # чтобы не было дублирования кода
# class FreelancersViewSet(viewsets.ModelViewSet):
#     serializer_class = FreelancersSerializer
#
#     # функция для отображения всего списка или по id
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Freelancers.objects.all()
#
#         return Freelancers.objects.filter(pk=pk)
#
# # декоратор action для формирования доп маршрутов
#     @action(methods=['get'], detail=True)
#     def category(self, request):
#         cats = Category.objects.get()
#         return Response({'cats': [c.name_category for c in cats]})




# class FreelancersApiView(APIView):
#     def get(self, request):
#         # формируется список из объектов класса Freelancers
#         f = Freelancers.objects.all()
#         # передаем список на сериализатор(как в функции encode); many=True - передаем несколько значений
#         # response - метод, преобразовывающий словарь posts, сформированный в views, в JSON строку
#         return Response({'posts': FreelancersSerializer(f, many=True).data})
#
#     def post(self, request):
#         # данные преобразованы в сериализатор
#         serializer = FreelancersSerializer(data=request.data)
#         # проверка перед добавлением в таблице
#         # raise_exception=True - выводит ошибку в виде JSON строки
#         serializer.is_valid(raise_exception=True)
#         # Вызывает метод create и добавляет запись в бд
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         # берем ключ из коллекции kwargs
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             # взять указанную запись из модели по ключу
#             instance = Freelancers.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = FreelancersSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         # вызовет метод update по аргументу instance
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         # берем ключ из коллекции kwargs
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             record = Freelancers.objects.get(pk=pk)
#             record.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"post": "delete post"+str(pk)})

# class FreelancersApiView(generics.ListAPIView):
 #   queryset = Freelancers.objects.all()
  #  serializer_class = FreelancersSerializer
