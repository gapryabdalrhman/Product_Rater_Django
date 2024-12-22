from django.urls import path
from rest_framework.routers import DefaultRouter  # for viewsets
from django.conf.urls import include
from .views import MealViewset,RatingViewset,home,UserViewSet

router = DefaultRouter()
router.register('meals',MealViewset)
router.register('ratings', RatingViewset)
router.register('users', UserViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('', home , name='home')
]