from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.LessonViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('<int:lesson_id>/questions', views.getQuestions),
    path('<int:lesson_id>/take', views.takeLesson)
]