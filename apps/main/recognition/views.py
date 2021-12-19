from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.viewsets import *
from .serializers import *
from ..user.models import BfrUser
from ..user.serializers import BfrUserSerializer


class UserRecognition(ViewSet):
    pass
