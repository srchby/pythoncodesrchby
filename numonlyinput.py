total = 0
s = 0
while total < 5:
  try:
      s += int(input('Enter a number: '))
  except ValueError:
      print ('Please only input numbers')
  else:
      total += 1



inp = int(input('Enter a number: '))
s = 0

try:
  s += inp
  if inp > 10:
    print('Please only input numbers below 10')
except ValueError:
  ("Please only input numbers")
else:
  print(s)