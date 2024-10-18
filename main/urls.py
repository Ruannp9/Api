from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, FuncionariosViewSet, TimeDeFutebolViewSet

router = DefaultRouter()
router.register(r'itens', ItemViewSet)
router.register(r'Funcionarios',FuncionariosViewSet )
router.register(r'TimeDeFutebol', TimeDeFutebolViewSet )


urlpatterns = [
    path('', include(router.urls))
]
