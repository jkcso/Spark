from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


# This is the non-technical user that needs the auth fields and a boolean field to say 'no' im not a dev.
class SimpleUser(models.Model):
    simple_user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_dev = models.BooleanField()

    @receiver(post_save, sender=User)
    def create_su(sender, instance, created, **kwargs):
        if created:
            SimpleUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_su(sender, instance, **kwargs):
        instance.profile.save()

    # Used for redirection to user profile after registration.
    def get_absolute_url(self):
        return reverse('user:profile_page', kwargs={'user_id': self.simple_user.user_id})  # previously: self.simple_user.user_id

    def __str__(self):
        return 'Developer? ->' + str(self.simple_user.is_dev) + ', id: ' + str(self.simple_user.user_id) + \
               ', username: ' + str(self.simple_user.username)


# This is the non-technical user that needs the auth fields and a boolean field to say 'no' im not a dev.
class Developer(models.Model):
    dev = models.OneToOneField(User, on_delete=models.CASCADE)

    # Captures developer's project type experience
    web = models.BooleanField()
    mobile = models.BooleanField()
    other_type = models.BooleanField()
    # in the view here you need a conditional: if other is true then please specify and enable the next field.
    specify_other_type = models.CharField(max_length=800)

    # Specifies if the developer was mostly working for back, front end, or both [radio buttons here].
    fe = models.BooleanField()
    be = models.BooleanField()
    full_stack = models.BooleanField()

    # Links to the developer profiles to provide other developers with the chance of finding more
    linkedin = models.BooleanField()
    linkedin_link = models.URLField(default='', blank=True)
    github = models.BooleanField()
    github_link = models.URLField(default='', blank=True)
    website = models.BooleanField()
    website_link = models.URLField(default='', blank=True)
    other_profile = models.BooleanField()
    specify_other_profile = models.URLField(default='', blank=True)

    @receiver(post_save, sender=User)
    def create_dev(sender, instance, created, **kwargs):
        if created:
            Developer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_dev(sender, instance, **kwargs):
        instance.profile.save()

    # Used for redirection to developer profile after registration.
    def get_absolute_url(self):
        return reverse('user:profile_page', kwargs={'user_id': self.dev.user_id})  # previously: self.dev.user_id

    def __str__(self):
        return 'Developer id: ' + str(self.dev.dev_id)
