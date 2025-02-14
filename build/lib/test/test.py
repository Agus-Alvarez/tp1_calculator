import unittest
import logging
from my_calculator_project.calculator.calculator import complex_calculator

class test_complex_calculator(unittest.TestCase):
    
    def test_add(self):
        c1 = complex_calculator(2, 3)
        c2 = complex_calculator(1, 1)
        result = c1.add(c2)
        self.assertEqual(result, (3, 4))
    
    def test_subtract(self):
        c1 = complex_calculator(2, 3)
        c2 = complex_calculator(1, 1)
        result = c1.subtract(c2)
        self.assertEqual(result, (1, 2))
    
    def test_multiply(self):
        c1 = complex_calculator(2, 3)
        c2 = complex_calculator(1, 1)
        result = c1.multiply(c2)
        self.assertEqual(result, (-1, 5))
    
    def test_divide(self):
        c1 = complex_calculator(2, 3)
        c2 = complex_calculator(1, 1)
        result = c1.divide(c2)
        self.assertEqual(result, (2.5, 0.5))
    
    def test_divide_by_zero(self):
        c1 = complex_calculator(2, 3)
        c2 = complex_calculator(0, 0)
        with self.assertRaises(ZeroDivisionError):
            c1.divide(c2)
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            complex_calculator('a', 3)  # Entrada no válida
    
    def test_invalid_add(self):
        c1 = complex_calculator(2, 3)
        c2 = 'invalid_input'  # Objeto no válido
        result = c1.add(c2)
        self.assertEqual(result, "ERROR: El objeto pasado no es un número complejo")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)  # Para que los logs se muestren
    unittest.main()
