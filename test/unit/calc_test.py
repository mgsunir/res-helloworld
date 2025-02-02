import pytest
import unittest

from app.calc import Calculator


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    # Test Ok sum
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(-4, self.calc.add(-2, -2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(1, self.calc.add(0, 1))
        self.assertEqual(0, self.calc.add(0, 0))

    # Las duplico para result1
    def test_add_method_returns_correct_result1(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(-4, self.calc.add(-2, -2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(1, self.calc.add(0, 1))
        self.assertEqual(0, self.calc.add(0, 0))
 
    # Test OK divide
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1.0, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(0.5, self.calc.divide(1, 2))
        self.assertEqual(2.0, self.calc.divide(4, 2))
        self.assertEqual(0, self.calc.divide(0, 2))
        # negatives
        self.assertEqual(-1, self.calc.divide(-2, 2))
        self.assertEqual(-1, self.calc.divide(2, -2))
        self.assertEqual(1, self.calc.divide(-2, -2))

        # Exceptions
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        
        
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, None, None)

        self.assertRaises(TypeError, self.calc.divide, "2", None)
        self.assertRaises(TypeError, self.calc.divide, None, "2")
        
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())
        self.assertRaises(TypeError, self.calc.divide, object(), object())

        self.assertRaises(TypeError, self.calc.divide, object(), "2")
        self.assertRaises(TypeError, self.calc.divide, "2", object())
        
        self.assertRaises(TypeError, self.calc.divide, None, object())
        self.assertRaises(TypeError, self.calc.divide, object(),None)

    ######################################################################
    # Test NOK add
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, None, None)

        self.assertRaises(TypeError, self.calc.add, "2", None)
        self.assertRaises(TypeError, self.calc.add, None, "2")

        
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
        self.assertRaises(TypeError, self.calc.add, object(), object())

        self.assertRaises(TypeError, self.calc.add, object(), "2")
        self.assertRaises(TypeError, self.calc.add, "2", object())
        
        self.assertRaises(TypeError, self.calc.add, None, object())
        self.assertRaises(TypeError, self.calc.add, object(),None)


    
        
    # Test NOK divide
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, None, None)

        self.assertRaises(TypeError, self.calc.divide, 2, object())
        self.assertRaises(TypeError, self.calc.divide, object(),2)
        self.assertRaises(TypeError, self.calc.divide, object(),object())
        
        self.assertRaises(TypeError, self.calc.divide, object(), "2")
        self.assertRaises(TypeError, self.calc.divide, "2", object())
        
        self.assertRaises(TypeError, self.calc.divide, None, object())
        self.assertRaises(TypeError, self.calc.divide, object(),None)

 # Test OK multiply
    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(0, 1))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(0, 0))
        
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(0, self.calc.multiply(0, -1))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(2, self.calc.multiply(-1, -2))
        
        # Pongo tambien casos negativois
        
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, None, None)

        self.assertRaises(TypeError, self.calc.multiply, "2", None)
        self.assertRaises(TypeError, self.calc.multiply, None, "2")

        
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
        self.assertRaises(TypeError, self.calc.multiply, object(), object())

        self.assertRaises(TypeError, self.calc.multiply, object(), "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", object())
        
        self.assertRaises(TypeError, self.calc.multiply, None, object())
        self.assertRaises(TypeError, self.calc.multiply, object(),None)

        
    # Exceptions multiply
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, None, None)

        self.assertRaises(TypeError, self.calc.multiply, "2", None)
        self.assertRaises(TypeError, self.calc.multiply, None, "2")

        
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
        self.assertRaises(TypeError, self.calc.multiply, object(), object())

        self.assertRaises(TypeError, self.calc.multiply, object(), "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", object())
        
        self.assertRaises(TypeError, self.calc.multiply, None, object())
        self.assertRaises(TypeError, self.calc.multiply, object(),None)

 ##########################-------------###########################    
    # Test OK power   
    def test_power_method_returns_correct_result(self):
        
        self.assertEqual(4, self.calc.power(2, 2))        
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(0, self.calc.power(0, 1))
        self.assertEqual(1, self.calc.power(0, 0))
        
        # Negatives
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(-1, self.calc.power(-1, -1))
        self.assertEqual(0.5, self.calc.power(2, -1))
        self.assertEqual(-27, self.calc.power(-3, 3))

        # Errors
        self.assertRaises(TypeError, self.calc.power, "0", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "0")
        self.assertRaises(TypeError, self.calc.power, "0", "2")
    
        self.assertRaises(TypeError, self.calc.power, 2, object())
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, object(), object())
        
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, None, None)

        self.assertRaises(TypeError, self.calc.power, "2", None)
        self.assertRaises(TypeError, self.calc.power, None, "2")
        
        self.assertRaises(TypeError, self.calc.power, "2", object())
        self.assertRaises(TypeError, self.calc.power, object(), "2")

        self.assertRaises(TypeError, self.calc.power, None, object())
        self.assertRaises(TypeError, self.calc.power, object(), None)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "0", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "0")
        self.assertRaises(TypeError, self.calc.power, "0", "2")
    
        self.assertRaises(TypeError, self.calc.power, 2, object())
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, object(), object())
        
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, None, None)

        self.assertRaises(TypeError, self.calc.power, "2", None)
        self.assertRaises(TypeError, self.calc.power, None, "2")
        
        self.assertRaises(TypeError, self.calc.power, "2", object())
        self.assertRaises(TypeError, self.calc.power, object(), "2")

        self.assertRaises(TypeError, self.calc.power, None, object())
        self.assertRaises(TypeError, self.calc.power, object(), None)

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(10, 6))
        self.assertEqual(-2, self.calc.substract(256, 258))
        self.assertEqual(-1, self.calc.substract(-1, 0))
        self.assertEqual(0, self.calc.substract(0, 0))        
        self.assertEqual(1, self.calc.substract(0, -1))
        self.assertEqual(0, self.calc.substract(-1, -1))
        self.assertEqual(-1, self.calc.substract(-3, -2))
 

        # NOK 
        self.assertRaises(TypeError, self.calc.substract, "0", 0)
        self.assertRaises(TypeError, self.calc.substract, "0", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "0")
        self.assertRaises(TypeError, self.calc.substract, "0", "2")
    
        self.assertRaises(TypeError, self.calc.substract, 2, object())
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, object(), object())
        
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, None, None)

        self.assertRaises(TypeError, self.calc.substract, None, "2")
        # self.assertRaises(TypeError, self.calc.substract, None, "2")
        
        # self.assertRaises(TypeError, self.calc.substract, "2", object())
        # self.assertRaises(TypeError, self.calc.substract, object(), "2")

        self.assertRaises(TypeError, self.calc.substract, None, object())
        self.assertRaises(TypeError, self.calc.substract, object(), None)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
