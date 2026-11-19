from calculator import Calculator

calculator = Calculator(op1=2.5, op2=5)
print(f"a={2.5} b={5}")

sum_result = calculator.sum()
print(f"Sum is equal: {sum_result}")

sub_result = calculator.subtract()
print(f"Substraction is equal: {sub_result}")

mul_result = calculator.multiply()
print(f"Multiplication is equal: {mul_result}")

try:
    div_result = calculator.divide()
    print(f"Division is equal: {div_result}")
except ZeroDivisionError:
    print(f"Division by zero!")

print("\n")

calculator2 = Calculator(op1=20, op2=0)
print(f"a={20} b={0}")

sum_result2 = calculator2.sum()
print(f"Sum is equal: {sum_result2}")

sub_result2 = calculator2.subtract()
print(f"Substraction is equal: {sub_result2}")

mul_result2 = calculator2.multiply()
print(f"Multiplication is equal: {mul_result2}")

try:
    div_result2 = calculator2.divide()
    print(f"Division is equal: {div_result2}")
except ZeroDivisionError:
    print(f"Division by zero!")
