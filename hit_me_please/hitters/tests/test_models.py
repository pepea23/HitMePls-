
from ..models import Hitter
from django.test import TestCase
# Create your tests here.
class HitterTest(TestCase):
    def test_hitter_model_should_have_email_field(self):
        hitter=Hitter.objects.create( email = "pepea.23@live.com")
        self.assertEqual(hitter.email,'pepea.23@live.com')
