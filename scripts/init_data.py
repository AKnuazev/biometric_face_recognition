import os
import sys

sys.path.append(os.path.join(os.path.dirname(sys.path[0])))  # , '..'))
print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")

import django

django.setup()

from django.db import transaction
from django.contrib.auth import get_user_model
from apps.main.user.models import BfrUser


@transaction.atomic
def create_init_data():
    # user = get_user_model()
    # user.objects.create_superuser(username='admin', password='123')
    user = BfrUser.objects.create_superuser(username='admin', name='Администратор', surname='Администраторов',
                                            otchestvo='Администраторович', password='123')


create_init_data()
print("Done!")
exit()
