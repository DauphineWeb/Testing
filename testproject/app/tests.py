from django.test import TestCase
from .models import Painting

# Create your tests here.
class TestPainting(TestCase):
    def setUp(self):
        Painting.objects.create(title='Mona Lisa', artist='Leonardo DaVinci', creation_year=1503)

    def test_1(self):
        self.assertEqual(Painting.objects.count(), 1)

