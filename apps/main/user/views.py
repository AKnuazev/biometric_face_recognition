from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.viewsets import *
from .serializers import *
import time
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
        if request.GET.get('camera_id') == '0':
            return Response({'success': False, 'err_msg': 'Фото некорректно, повторите попытку!'})

        res = RecognizationService.make_photo(1)
        if not res:
            err_msg = "Фото некорректно, повторите попытку!"
            return Response({'success': res, 'err_msg': err_msg})

        time.sleep(3)
        RecognizationService.make_photo(2)

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
        data['acl'] = user_obj.acl
        print(f'Распознал {user}')
        return Response({'success': True, 'data': data})

    @action(detail=False)
    def take_photo(self, request, pk=None):
        if not request.GET.get('camera_id'):
            return Response({'success': False, 'err_msg': 'Камера не указана'})
        camera_id = int(request.GET.get('camera_id'))

        res = RecognizationService.make_photo(camera_id)
        if not res:
            err_msg = "Фото некорректно, повторите попытку!"
            return Response({'success': res, 'err_msg': err_msg})
        return Response({'success': res})

    @action(detail=False)
    def save_current(self, request, pk=None):
        user_id = request.GET.get('user_id')
        if not user_id:
            return Response({'success': False, 'err_msg': 'Пользователь не указан'})

        RecognizationService.save_current_image(user_id)
        return Response()

    @action(detail=False)
    def check_current(self, request, pk=None):
        res = RecognizationService.check_image()
        return Response({'res': res})

    @action(detail=False)
    def learn(self, request, pk=None):
        RecognizationService.face_train()
        return Response()

