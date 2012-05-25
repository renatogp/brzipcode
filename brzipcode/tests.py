# coding: utf-8
from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.utils import simplejson


class CoreTestCase(unittest.TestCase):

    def setUp(self):
        self.url = reverse('brzipcode_view')
        self.client = Client()

    def _get_zip_code(self, zip_code):
        return self.client.get("%s?zip_code=%s" % (self.url, zip_code))

    def test_valid_zip_code(self):
        response = self._get_zip_code('14030360')
        r = simplejson.loads(response.content)

        self.assertEqual(r.get('status'), True)
        self.assertEqual(r.get('state'), u'SP')
        self.assertEqual(r.get('neighborhood'), u'Jardim Maria Goretti')
        self.assertEqual(r.get('city'), u'Ribeirão Preto')
        self.assertEqual(r.get('address'), u'Rua Aloísio de Azevedo')
        self.assertEqual(r.get('zip_code'), u'14030360')

    def test_invalid_zip_code(self):
        response = self._get_zip_code('00000000')
        r = simplejson.loads(response.content)

        self.assertEqual(r.get('status'), False)
        self.assertEqual(r.get('message'), u'not_found')
