from django.test import TestCase
from . import factories


class BrandTest(TestCase):
    def test_str(self):
        brand = factories.BrandFactory(name='nike')
        self.assertEqual(str(brand), 'nike')


class LabelTest(TestCase):
    def test_str(self):
        label = factories.LabelFactory(name='air')
        self.assertEqual(str(label), 'air')
