from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None):
        if not mobile:
            raise ValueError('Users must have an mobile')

        user = self.model(mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, password=None):
        user = self.create_user(mobile=mobile, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
