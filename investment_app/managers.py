from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, isInvestor, isOwner, address):
        user = self.model(email=email, password=password, isInvestor=isInvestor, isOwner=isOwner, address=address)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, isInvestor, isOwner):
        user = self.create_user(email=email, password=password, isInvestor=isInvestor, isOwner=isOwner)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)

