import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalciulator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""
    def setUp(self):
        """Set up a SimplCalculator instance for testing."""
        self.calc = SimpleCalculator()


    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -10), -15)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -10), 5)
        self.assertEqual(self.calc.subtract(3, 0), 3)
    
    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(-2, -5), 10)
    
    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5, -2), -2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)

        #Test division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")


if __name__ == "__main__":
    unittest.main()
        
