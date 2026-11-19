class Calculator:
    """Class calculator"""
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        """Function printing sum"""
        return self.op1 + self.op2

    def subtract(self):
        """Function printing subtract"""
        return self.op1 - self.op2

    def multiply(self):
        """Function printing multiply"""
        return self.op1 * self.op2

    def divide(self):
        """Function printing divide"""
        if self.op2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.op1/self.op2
