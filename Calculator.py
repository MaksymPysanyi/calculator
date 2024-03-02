import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль неможливе")
        return a / b
    

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        a, b = 5, 3
        result = self.calculator.add(a, b)
        self.assertEqual(result, 8, "Sum of 5 and 3 should be 8")

    def test_add_negative_numbers(self):
        # Arrange
        a, b = -5, -3

        # Act
        result = self.calculator.add(a, b)

        # Assert
        self.assertEqual(result, -8, "Сума -5 і -3 має бути -8")

    def test_multiply_positive_numbers(self):
        # Arrange
        a, b = 5, 3

        # Act
        result = self.calculator.multiply(a, b)

        # Assert
        self.assertEqual(result, 15, "Добуток 5 і 3 має бути 15")
    
    def test_divide_positive_numbers(self):
        # Arrange
        a, b = 5, 3

        # Act
        result = self.calculator.divide(a, b)

        # Assert
        self.assertEqual(result, 1.66667, "Результат ділення 5 на 3 має бути 1.66667")

if __name__ == "__main__":
    unittest.main()

calculator = Calculator()
result = calculator.subtract(-5, -3)
print ('Sum:', result)