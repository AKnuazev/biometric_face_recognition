from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.viewsets import *
from .serializers import *
from recognizer.Recognizer import RecognizationService


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

    def perform_destroy(self, instance):
        RecognizationService.delete_image(instance.pk)
        instance.delete()


    @action(detail=False)
    def login(self, request, pk=None):
        res = RecognizationService.make_photo()
        if not res:
            err_msg = "Фото некорректно, повторите попытку!"
            return Response({'success': res, 'err_msg': err_msg})
        print('норм')
        user = RecognizationService.check_image()
        if not user:
            err_msg = "Неизвестный пользователь!"
            return Response({'success': False, 'err_msg': err_msg})
        data = {}
        user_obj = BfrUser.objects.filter(pk=user).first()
        data['id'] = user
        data['ФИО'] = user_obj.get_full_name()
        data['email'] = user_obj.email
        data['Телефон'] = user_obj.telephone
        data['username'] = user_obj.username
        return Response({'success': True, 'data': data})

    @action(detail=False)
    def take_photo(self, request, pk=None):
        res = RecognizationService.make_photo()
        if not res:
            err_msg = "Фото некорректно, повторите попытку!"
            return Response({'success': res, 'err_msg': err_msg})
        return Response({'success': res})

    @action(detail=False)
    def save_current(self, request, pk=None):
        RecognizationService.save_current_image()
        return Response()

    @action(detail=False)
    def check_current(self, request, pk=None):
        res = RecognizationService.check_image()
        return Response({'res': res})

    @action(detail=False)
    def learn(self, request, pk=None):
        RecognizationService.face_train()
        return Response()

    @action(detail=False)
    def create_new(self, request, pk=None):
        RecognizationService.face_train()
        return Response()
