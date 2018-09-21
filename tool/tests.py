from django.test import TestCase
import requests

class FirstTest(TestCase):
    def test_aa(self):
        urls = 'http://127.0.0.1:8000'
        r = requests.get(urls)

    def test_httpheader_post(self):
        urls = 'http://127.0.0.1:8000/httpheader'
        r = requests.post(urls)

# Create your tests here.
