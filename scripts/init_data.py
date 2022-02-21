import os
import sys

sys.path.append(os.path.join(os.path.dirname(sys.path[0])))  # , '..'))
print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")

import django

django.setup()

from django.db import transaction
from apps.main.user.models import BfrUser, BfrDoor, BfrSystem


@transaction.atomic
def create_init_data():
    BfrSystem.objects.create(emergency_mode=False)
    user = BfrUser.objects.create_superuser(username='admin', name='Администратор', surname='Администраторов',
                                            otchestvo='Администраторович', email='admin@example.com',  password='123')
    door_1 = BfrDoor.objects.create(code=1, name='Главная дверь')
    door_2 = BfrDoor.objects.create(code=2, name='Второй этаж')
    door_3 = BfrDoor.objects.create(code=3, name='Третий этаж')


create_init_data()
print("Done!")
exit()
