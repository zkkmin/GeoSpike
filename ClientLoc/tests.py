from django.test import TestCase, RequestFactory
from django.test import Client
from . import views

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_get_country(self):
        request = self.factory.get('/country/')
        # request.META.get('REMOTE_ADDR')
        request.META['REMOTE_ADDR'] = "103.224.165.57"
        
        response = views.get_country(request)
        self.assertEqual(response.status_code, 200)