from django.test import TestCase, Client
from .models import Order


class M23ViewTestСase(TestCase):
    """Класс тестирования представлений m23_app"""

    def test_index(self):
        """Тестирование домашней страницы"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_services(self):
        """Тестирование страницы 'услуг'."""
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)

    def test_about_us(self):
        """Тестирование страницы 'о нас'."""
        response = self.client.get('/about_us')
        self.assertEqual(response.status_code, 200)

    def test_contacts(self):
        """Тестирование страницы 'контакты'."""
        response = self.client.get('/contacts')
        self.assertEqual(response.status_code, 200)

    def test_new_order(self):
        """Тестирование страницы создания заказа"""
        response = self.client.get('/new_order')
        self.assertEqual(response.status_code, 200)
