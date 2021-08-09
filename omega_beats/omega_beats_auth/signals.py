from django.db.models.signals import post_save
from django.dispatch import receiver
from omega_beats.omega_beats_auth.models import OmegaBeatsUser, Profile


@receiver(post_save, sender=OmegaBeatsUser)
def create_profile(sender, instance, created, **kwargs):
    """
    A signal used to create a profile entity, hooked with the User upon registration.
    """

    if created:
        Profile(
            user=instance,
        ).save()
