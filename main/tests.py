from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_template_contains_name_and_class(self):
        response = self.client.get('/main/')
        self.assertContains(response, 'Name: Vina Myrnauli Abigail Siallagan')
        self.assertContains(response, 'Class: PBP E')

    def test_template_contains_title(self):
        response = Client().get('/main/')
        self.assertContains(response, '<title>SCOOBYRIA</title>')

    def test_template_contains_images(self):
        response = Client().get('/main/')
        self.assertContains(response, '<img src="/static/foodie.png"')
        self.assertContains(response, '<img src="/static/drink.png"')