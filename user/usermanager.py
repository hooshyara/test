from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("phone and password must be provided")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, password, **extra_fields)
    
    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self._create_user(username, password, **extra_fields)