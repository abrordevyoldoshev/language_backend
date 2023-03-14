from rest_framework import viewsets
# Create your views here.
from .models import LanguageTodo, Category
from .serializers import LanguageSerializers, CategorySerializers


class TodoAllApiView(viewsets.ModelViewSet):
    queryset = LanguageTodo.objects.all()
    serializer_class = LanguageSerializers
    lookup_field = 'id'


class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = 'id'
