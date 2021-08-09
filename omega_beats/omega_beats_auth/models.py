from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models


class OmegaBeatManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, password, **extra_fields)


class OmegaBeatsUser(AbstractBaseUser, PermissionsMixin):
    """
    Extending the UserModel to use email and password for authentication.
    """

    email = models.EmailField(
        unique=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = OmegaBeatManager()


class Profile(models.Model):
    """
    User's profile entity used to store all the information displayed to the other users.
    """

    username = models.CharField(
        max_length=30,
        blank=True,
        default='default username',
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        default='default description',
    )

    avatar_image = models.ImageField(
        upload_to='avatars',
        blank=True,
    )

    user = models.OneToOneField(
        OmegaBeatsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.username}, owned by {self.user.email}'
