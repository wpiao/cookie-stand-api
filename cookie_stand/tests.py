# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from .models import CookieStand


# class CookieStandTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         testuser = get_user_model().objects.create_user(username='testuser', password='pass')
#         testuser.save()

#         test_cookiestand = CookieStand.objects.create(location='Seattle', owner=testuser, description='Seattle')
#         test_cookiestand.save()

#     def test_cookiestand_model(self):
#         cookie_stand = CookieStand.objects.get(id=1)
#         self.assertEqual(str(cookie_stand.owner), 'testuser')
#         self.assertEqual(str(cookie_stand.location), 'Seattle')
#         self.assertEqual(str(cookie_stand.description), 'Seattle')