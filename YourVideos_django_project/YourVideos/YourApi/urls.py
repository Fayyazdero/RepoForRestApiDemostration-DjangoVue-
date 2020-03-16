from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import VideoViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]