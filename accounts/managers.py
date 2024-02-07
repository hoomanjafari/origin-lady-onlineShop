from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **other_fields):
        if not mobile:
            raise ValueError('لطفا شماره موبایل خود را وارد کنید !')
        user = self.model(
            mobile=mobile,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, mobile, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('for Superuser is_staff option should be True !')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('for Superuser is_superuser option should be True !')
        return self.create_user(mobile, password, **other_fields)
