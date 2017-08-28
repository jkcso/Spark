# from django.test import TestCase
# from .models import SimpleUser, Developer, User
#
#
# class TestUser(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         '''
#
#         stack overflow same error: https://stackoverflow.com/questions/15942939/django-typeerror-username-is-an-invalid-keyword-argument-for-this-function
#
#         user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
#                                         password=form.cleaned_data['password'])
#         user.save()
#         employee = Employee(user=user, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
#         '''
#
#         cls.simple_user = User.objects.create_user(username='u1', email='u1@mail.com', password='1234',
#                                                    first_name='f1_name', last_name='s1_name')
#
#         cls.u1 = SimpleUser.objects.create(simple_user=cls.simple_user, is_dev=False)
#
#         # cls.su = SimpleUser.objects.create(u1, is_dev=False)
#
#         # cls.dev = Developer.objects.create(email='u2@mail.com', password='5678',
#         #                                    first_name='f2_name', last_name='s2_name',
#         #                                    web=True, mobile=False, other_type=False,
#         #                                    fe=True, be=False, full_stack=False,
#         #                                    linkedin=True, linkedin_link='www.lk.com/id=1',
#         #                                    github=True, github_link='www.gh.com/id=1',
#         #                                    website=False, website_link=False, other_profile=False)
#
#     # Tests db insertion
#     def test_db_insertion(self):
#         pass
#
#     #
#     def test_db_incremental_id(self):
#         pass
#
#     #
#     def test_db_field_modification(self):
#         pass
