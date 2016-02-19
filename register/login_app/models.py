# from __future__ import unicode_literals
# from django.contrib.auth.models import User
#
# from django.db import models
# from django.conf import settings
#
#
# class Signup(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#
#     class Meta:
#         verbose_name_plural = 'Signup'
#         User._meta.get_field('email')._unique = True
#
#     def __str__(self):
#         return self.user.username
#
#
# class Test(models.Model):
#     """
#     this class test is used to test whether the user.met_email_unique is assigned in Signup model is reflected
#     in test model
#     Note:meta_field of email unique is reflecting  in Test model because of User is unique changes will happen to all
#
#     """
#     user_test = models.OneToOneField(settings.AUTH_USER_MODEL)
#
#     class Meta:
#         pass
#
#     def __str__(self):
#         return self.user_test.username
