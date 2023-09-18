from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_contains_table_header(self):
        response = Client().get('')
        self.assertContains(response, '<th>Name</th>', html=True)
        self.assertContains(response, '<th>Price</th>',html=True)
        self.assertContains(response, '<th>Description</th>', html=True)
     
        
        