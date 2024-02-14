from django.contrib.auth.backends import ModelBackend
from .models import MyUser


class MobileAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, mobile=None):
        try:
            user = MyUser.objects.get(mobile=mobile)
            if user.check_password(password):
                return user
            else:
                return None
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None
