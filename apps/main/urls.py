from rest_framework.routers import DefaultRouter
from .user.views import CurrentUserViewSet, UsersViewSet, BfrRoomViewSet
from .recognition.views import UserRecognitionViewSet

main_router = DefaultRouter(trailing_slash=False)
main_router.register(r'main/current_user', CurrentUserViewSet, basename='current_user')
main_router.register(r'main/users', UsersViewSet)
main_router.register(r'main/rooms', BfrRoomViewSet)


