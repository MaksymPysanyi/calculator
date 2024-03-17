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
    
    def power(self, a, b):
        return a ** b

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        return a * b // self.gcd(a, b)
    

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
    def test_calculate_power(self):
        calculator = Calculator()
        self.assertEqual(calculator.power(5, 3), 125)

    def test_gcd(self):
        calculator = Calculator()
        self.assertEqual(calculator.gcd(12, 18), 6)
        self.assertEqual(calculator.gcd(15, 25), 5)
        self.assertEqual(calculator.gcd(21, 28), 7)

    def test_lcm(self):
        calculator = Calculator()
        self.assertEqual(calculator.lcm(12, 18), 36)
        self.assertEqual(calculator.lcm(15, 25), 75)
        self.assertEqual(calculator.lcm(21, 28), 84)
    
 

if __name__ == "__main__":
    unittest.main()

calculator = Calculator()
result = calculator.subtract(-5, -3)
print ('Sum:', result)
