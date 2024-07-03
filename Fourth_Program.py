class Calculator:
  """
  A simple calculator class for basic arithmetic operations.
  """

  def __init__(self):
    self.operations = {"+": self.add, "-": self.subtract, "*": self.multiply, "/": self.divide}

  def get_user_input(self):
    """
    Prompts the user for input and validates it.

    Returns:
      A tuple containing the first number, operator, and second number as floats, or None if invalid input is provided.
    """
    while True:
      try:
        expression = input("Enter expression (num1 operator num2): ")
        num1, operator, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)
        if operator not in self.operations:
          raise ValueError("Invalid operator")
        return num1, operator, num2
      except ValueError as e:
        print(f"Invalid input: {e}")

  def calculate(self):
    """
    Gets user input, validates it, and performs the chosen operation.

    Prints the result or an error message if the input is invalid.
    """
    num1, operator, num2 = self.get_user_input()
    if num1 is not None:
      result = self.operations[operator](num1, num2)
      print(f"{num1} {operator} {num2} = {result}")

  def add(self, a, b):
    """
    Performs addition operation.
    """
    return a + b

  def subtract(self, a, b):
    """
    Performs subtraction operation.
    """
    return a - b

  def multiply(self, a, b):
    """
    Performs multiplication operation.
    """
    return a * b

  def divide(self, a, b):
    """
    Performs division operation, handling division by zero.
    """
    if b == 0:
      print("Error: Division by zero")
      return None
    return a / b

# Create a calculator object and run the calculation loop
calculator = Calculator()
while True:
  calculator.calculate()
  user_choice = input("Do you want to calculate again? (y/n): ")
  if user_choice.lower() != "y":
    break

print("Thank you for using the calculator!")
