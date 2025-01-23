class Calculator:
    # Class attribute to demonstrate access by class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to perform addition."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to perform multiplication and access class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
