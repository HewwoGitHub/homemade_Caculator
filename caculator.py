def startEquation3():
  global answer
  if operation == "+":
      answer = num1 + num2 + num3
      print("The Answer is " + str(answer))

  elif operation == "-":
      answer = num1 - num2 - num3
      print("The Answer is " + str(answer))

  elif operation == "*":
      answer = num1 * num2 * num3
      print("The Answer is " + str(answer))

  elif operation == "/":
      answer = num1 / num2 / num3
      print("The Answer is " + str(answer))
  else:
      print("Invalid operation")

def startEquation():
  global answer
  if operation == "+":
      answer = num1 + num2
      print("The Answer is " + str(answer))

  elif operation == "-":
      answer = num1 - num2
      print("The Answer is " + str(answer))

  elif operation == "*":
      answer = num1 * num2
      print("The Answer is " + str(answer))

  elif operation == "/":
      answer = num1 / num2
      print("The Answer is " + str(answer))
  else:
      print("Invalid operation")

while True:
  operation = input('What Operation would you like to do? (+, -, *, /) ')

  if operation not in ['+', '-', '*', '/']:
      print('Invalid Operation')
      continue

  num1_input = input('Enter the first number: ')
  num2_input = input('Enter the second number: ')
  more_numbers = input('Do you want to add another number (y/n | you can only add one number) ')

  if more_numbers == 'y':
      num3_input = input('Enter the third number: ')
      if num1_input.isdigit() and num2_input.isdigit() and num3_input.isdigit():
          num1 = int(num1_input)
          num2 = int(num2_input)
          num3 = int(num3_input)
          startEquation3()
      else:
          print("Some Inputs are not a number")
  else:
      if num1_input.isdigit() and num2_input.isdigit():
          num1 = int(num1_input)
          num2 = int(num2_input)
          startEquation()
      else:
          print("Some Inputs are not a number")

  restart = input('Do you want to restart the program? (yes/no): ')
  if restart.lower() != 'yes':
      break
