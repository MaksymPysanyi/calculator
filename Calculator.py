import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add_positive_numbers(self):
        a, b = 5, 3
        result = self.calculator.add(a, b)
        self.assertEqual(result, 8, "Sum of 5 and 3 should be 8")

if __name__ == "__main__":
    unittest.main()

calculator = Calculator()
result = calculator.add(5, 3)
print ('Sum:', result)