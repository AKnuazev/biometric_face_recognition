from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.viewsets import *
from recognizer.Recognizer import RecognizationService


class UserRecognitionViewSet(ViewSet):
    pass
