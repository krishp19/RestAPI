from rest_framework import routers
from .viewsets import UserViewSet,ProfileViewSet

app_name = "user"

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('Profile',ProfileViewSet)