
from project import app, LBTT_calculator
import project as pj
import pytest
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_function(self):
        tester = app.test_client(self)
        self.assertEqual(LBTT_calculator(1100000), 88250 )

    def test_function1(self):
        tester = app.test_client(self)
        self.assertEqual(LBTT_calculator(600000), 31250 )

    def test_function2(self):
        tester = app.test_client(self)
        self.assertEqual(LBTT_calculator(200000), 0)
    
    
    def test_function3(self):
        tester = app.test_client(self)
        self.assertEqual(LBTT_calculator(400000), 11250)



    

    



if __name__ == '__main__':
    unittest.main()