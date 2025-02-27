from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, World!')

class DomainRedirectMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_no_redirect_non_fly_domain(self):
        response = self.client.get(reverse('home'), HTTP_HOST='api.travelstreamapp.com')
        self.assertEqual(200, response.status_code)

    def test_redirect_fly_domain(self):
        response = self.client.get(reverse('home'), HTTP_HOST=f"travel-stream.fly.dev")
        self.assertEqual(301, response.status_code)
        self.assertEqual('https://api.travelstreamapp.com/', response['Location'])
