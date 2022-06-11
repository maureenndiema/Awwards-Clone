from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user=User(username='maureen')
        self.user.save()
        self.profile=Profile(user=self.user,name='chela',bio='lagom',prof_pic='',location='kenya',account_url='www.chela.com')
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
    def test_instance(self):
         self.assertTrue(isinstance(self.profile, Profile))

    def test_saveProfile(self):
        self.profile.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)
    def test_delete_method(self):


        self.user.delete()
        profile = User.objects.all()
        self.assertTrue(len(profile) == 0)

