from django.test import TestCase
from adoptions.models import Pet

class PetTestCase(TestCase):
    def setUp(self):
        Pet.objects.create(name="lion", submission_date="2020-12-10")
        Pet.objects.create(name="cat", submission_date="2020-10-10")

    def test_pet_can_create(self):
        """Pets that can create"""
        lion = Pet.objects.get(name="lion")
        cat = Pet.objects.get(name="cat")
        self.assertEqual(lion.name, 'lion')
        self.assertEqual(cat.name, 'cat')