from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.viewsets import *
from .serializers import *


class CurrentUserViewSet(ViewSet):
    """
    Возвращает данные текущего пользователя
    """

    def list(self, request):
        user_data = BfrUserSerializer(request.user).data
        return Response(data=user_data)


class UsersViewSet(BfrModelViewSet):
    queryset = BfrUser.objects.all()
    serializer_class = BfrUserSerializer

