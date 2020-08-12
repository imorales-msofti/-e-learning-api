from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.CourseViewSet)
urlpatterns = router.urls

urlpatterns.append(
    path('<int:course_id>/lessons', views.getLessons)
)