from colorama import Fore

print(Fore.MAGENTA + '\n Calculator made by Srcµ.')
print('\033[39m')

def addition (a,b):
  return a + b

def subtraction (a,b):
  return a - b

def division (a,b):
  if b == 0:
    print(Fore.RED + '\n Can\'t divide a number by zero')
    print('\033[39m')
    return 0
  return a / b

def multiply (a,b):
  return a * b

while True:
  print('\n Please select a operation:')
  print('\n 1. addition')
  print('\n 2. subtraction')
  print('\n 3. division')
  print('\n 4. multiply')
  print('\n 5. quit the calculator')

  choice = input('\n')

  if choice in ('q', 'quit', 'leave', '5'):
    break

  if choice in ['1', '2', '3', '4']:
    try:
      num1 = int(input('\n Please input first number: '))
      num2 = int(input('\n Please input second number: '))
    except ValueError:
      print(Fore.RED + "\n Please only enter valid input")
      print('\033[39m')
      continue
  
  if choice == '1':
    print(addition(num1,num2))

  elif choice == '2':
    print(subtraction(num1,num2))
    
  elif choice == '3':
    print(division(num1,num2))
    
  elif choice == '4':
    print(multiply(num1,num2))

  else:
    print(Fore.RED + '\n It seems you have entered a invalid input, please try again')
    print('\033[39m')