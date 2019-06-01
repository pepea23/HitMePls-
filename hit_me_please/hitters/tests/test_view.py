from django.test import TestCase
from ..models import Hitter


class LandingPageViewTest(TestCase):
    def test_view_should_have_from_wit_enail_field_and_submit_button(self):
        response = self.client.get('/')
        expected = '<form action = "." method ="post">'
        self.assertContains(response, expected, status_code=200)
        expected = '<input type="hidden" name="csrfmiddlewaretoken"'
        self.assertContains(response, expected, status_code=200)
        expected = '<input type ="email" name="email" />'
        self.assertContains(response, expected, status_code=200)
        expected = '<button type ="submit" >Sunbmit </button>'
        self.assertContains(response, expected, status_code=200)

    def test_view_should_have_submit_form(self):

        data = {
            'email': 'pepea.23@live.com'
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code,200)
        count = Hitter.objects.filter(email="pepea.23@live.com").count()
        self.assertEqual(count, 1)
