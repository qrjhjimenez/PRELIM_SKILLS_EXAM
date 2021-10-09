from number2 import Temperature
import unittest

class test_number2(unittest.TestCase):
    def test_celsius(self):
        value = Temperature(celsius=15).kelvin 
        result = 273.15 + 15
        self.assertEqual(value,result)

    def test_fahrentheit(self):
        value = Temperature(fahrenheit=100).kelvin
        result = (100 - 32) * 5/9 + 273.15
        self.assertEqual(value,result)

    def test_kelvin(self):
        value = Temperature(kelvin=15).kelvin
        result = 15
        self.assertEqual(value,result)

    def test_negative(self):
        def negative():
            value = Temperature(-1)
            with self.assertRaises(ValueError):
                negative(value)
        
if __name__ == '__main__':
    unittest.main()