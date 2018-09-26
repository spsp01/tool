from django.test import TestCase
import requests
from tool.models import Client

class FirstTest(TestCase):


    def test_aa(self):
        urls = 'http://127.0.0.1:8000'
        r = requests.get(urls)

    def test_httpheader_post(self):
        urls = '/httpheader'
        r = self.client.get(urls)


    def test_add_client(self):
        Client.objects.create(name="lion")

# Create your tests here.
