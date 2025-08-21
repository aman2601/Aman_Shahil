class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            return self.a / self.b if self.b != 0 else "Division by zero"
        else:
            return "Invalid operation"

calc = Calculator(1546, 4587)
print(calc.calculate('multiply'))

