from main import app
import unittest

class FlaskTestCase(unittest.TestCase):

    #Prueba unitaria para el metodo main
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(b'<h1>LABORATORIO 11 - AYD1</h1>', response.data)

if __name__ == '__main__':
    unittest.main()