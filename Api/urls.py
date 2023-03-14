from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TodoAllApiView,CategoryApiView

router = DefaultRouter()

router.register('todo_all', TodoAllApiView, basename='todo_list')
router.register('category', CategoryApiView, basename='category_list')
urlpatterns = router.urls
