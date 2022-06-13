from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class ProfileTest(TestCase):
    def setUp(self):
        self.kate = User(user = 'kate',bio = 'la vida loca')
        self.kate = Profile(user = Self.kate,user_id = 1,bio = 'my awards',image = 'image.jpg',date_created='Jun,13.2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.kate,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.kate.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)





