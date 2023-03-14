from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class LanguageTodo(models.Model):
    rus_title = models.CharField(max_length=150)
    uzb_title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rus_title} -- {self.uzb_title}"


