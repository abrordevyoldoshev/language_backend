from rest_framework import serializers
from .models import Category, LanguageTodo


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = LanguageTodo
        fields = ('id', 'rus_title', 'uzb_title','category')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

