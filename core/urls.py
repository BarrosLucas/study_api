from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DisciplineViewSet, StudySessionViewSet

router = DefaultRouter()
router.register(r'disciplines', DisciplineViewSet)
router.register(r'study-sessions', StudySessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
