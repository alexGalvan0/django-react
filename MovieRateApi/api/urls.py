from django.contrib import admin
from django.urls import path
from .views import MovieViewSet,RatingViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('ratings',RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
