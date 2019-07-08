from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_rooturl_resolveto_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_return_correcthtml(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))