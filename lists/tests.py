from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_rooturl_resolveto_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)