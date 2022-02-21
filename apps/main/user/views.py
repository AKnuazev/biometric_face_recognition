from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.viewsets import *
from .serializers import *
import time
from recognizer.Recognizer import RecognizationService
import logging
from datetime import datetime


class CurrentUserViewSet(ViewSet):
    """
    Возвращает данные текущего пользователя
    """

    def list(self, request):
        user_data = BfrUserSerializer(request.user).data
        return Response(data=user_data)


class BfrRoomViewSet(BfrModelViewSet):
    queryset = BfrDoor.objects.all()
    serializer_class = BfrDoorSerializer


class UsersViewSet(BfrModelViewSet):
    queryset = BfrUser.objects.all()
    serializer_class = BfrUserSerializer

    def perform_destroy(self, instance):
        RecognizationService.delete_image(instance.pk)
        instance.delete()

    @action(detail=False)
    def login(self, request, pk=None):
        system = BfrSystem.objects.get(pk=1)
        if system.emergency_mode:
            return Response({'success': True, 'data': 'АВАРИЙНЫЙ РЕЖИМ! ПРОХОД РАЗРЕШЁН!'})

        if not request.GET.get('is_entrance') and not request.GET.get('door_id'):
            return Response({'success': False, 'err_msg': 'Некорректный запрос!'})
        is_entrance = True if request.GET.get('is_entrance') == '1' else False
        door = BfrDoor.objects.filter(pk=request.GET.get('door_id')).first()
        if not door:
            return Response({'success': False, 'err_msg': 'Некорректный запрос!'})

        if request.GET.get('camera_id') == '0':
            time.sleep(3)
            return Response({'success': False, 'err_msg': 'Фото некорректно, повторите попытку!'})

        res = RecognizationService.make_photo(1)
        if not res:
            err_msg = "Фото некорректно, повторите попытку!"
            return Response({'success': res, 'err_msg': err_msg})
        RecognizationService.make_photo(2)

        logging.basicConfig(filename='login.log', level=logging.INFO,  format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        user = RecognizationService.check_image()
        if not user:
            err_msg = "Неизвестный пользователь!"
            logging.info('Неизвестный пользователь попытался войти через {}[id: {}]'.format(door.name, door.code))
            return Response({'success': False, 'err_msg': err_msg})

        user_obj = BfrUser.objects.filter(pk=user).first()
        if door in user_obj.acl.all():
            if is_entrance:
                user_obj.last_indoor = door
                user_obj.indoor_time = datetime.now()
                user_obj.save()
                serializer = BfrUserSerializer(user_obj)
                logging.info(
                    'Пользователь {} [id: {}] вошел через {} [id: {}]'.format(user_obj.get_full_name(), user_obj.pk,
                                                                              door.name, door.code))
            else:
                user_obj.last_outdoor = door
                user_obj.outdoor_time = datetime.now()
                user_obj.save()
                serializer = BfrUserSerializer(user_obj)
                logging.info(
                    'Пользователь {} [id: {}] вышел через {} [id: {}]'.format(user_obj.get_full_name(), user_obj.pk,
                                                                              door.name, door.code))
            return Response({'success': True, 'data': serializer.data})
        else:
            logging.info(
                'Пользователь {} [id: {}] попытался войти через {} [id: {}], но у него нет доступа'.format(user_obj.get_full_name(), user_obj.pk,
                                                                          door.name, door.code))
            return Response({'success': False, 'err_msg': 'Уважаемый {}, у вас нет доступа к {}'.format(user_obj.get_full_name(), door.name)})


    @action(detail=False)
    def take_photo(self, request, pk=None):
        if not request.GET.get('camera_id'):
            # return Response({'success': False, 'err_msg': 'Камера не указана'})
            camera_id = 1
        else:
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

    @action(detail=False)
    def test(self, request, pk=None):
        RecognizationService.test()
        return Response()

