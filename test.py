from django.test import TestCase
from django.urls import reverse

class TestHomePage(TestCase):

    def test_home_page_status_code(self):
        """
        Home sahifasi ochilishi va HTTP 200 qaytarishini tekshiradi
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        """
        Home sahifasi to‘g‘ri template ishlatayotganini tekshiradi
        """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_content(self):
        """
        Home sahifasida 'Home page' matni borligini tekshiradi
        """
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Home pages</h1>')
