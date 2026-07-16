num1= int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

operator = input("Enter an operator (+, -, *, /): ")

match operator:
  case "+":
    result = num1 + num2
  case "-":
    result = num1 - num2
  case "*":
    result = num1 * num2
  case "/":
    result = num1 / num2
print("The result is: ", result)