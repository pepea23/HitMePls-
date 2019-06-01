from django.contrib import admin
from django.test import TestCase

from .admin import HitterAdmin
from .models import Hitter

# Create your tests here.
class HitterTest(TestCase):
    def test_hitter_model_should_have_email_field(self):
        hitter=Hitter.objects.create( email = "pepea.23@live.com")
        self.assertEqual(hitter.email,'pepea.23@live.com')

class HitterAdminTest(TestCase):
    def test_hitter_should_be_register_to_admin(self):
        self.assertIsInstance (admin.self._registry[Hitter],HitterAdmin)
            
    def test_hitter_admin_should_set_list_display(self):
        expected=(
            'email',
        )
        self.assertEqual  (HitterAdmin.list_display,expacted)