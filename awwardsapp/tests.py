from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user=User(username='alvynah')
        self.user.save()
        self.profile=Profile(user=self.user,name='vee',bio='vee in the house',prof_pic='default.png',location='kenya',account_url='www.alvynah.com')
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
    def test_instance(self):
         self.assertTrue(isinstance(self.profile, Profile))
