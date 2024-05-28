#if the name is not a letter, output print then break
while True:
  name = input('Please input your name: ')
  if name.isalpha():
    name = str(name)

  #output then break
  else:
    print('Please only input characters')
    exit()
  break

#if the age is not a number, output print then break
while True:
  age = (input('Please input your age: '))
  if age.isdigit():
    age = int(age)

    #if the age is higher or equal to 20 AND lower or equal to 100, output print
    if 20 <= age <= 100:
      print('you\'re old')

    #if age higher than 100, output print
    elif age > 100:
      print('too old')

    #if age higher than 0 and lower than 20, output print
    elif 0 < age < 20:
      print('you\'re young')

    #if age lower or equal to 0, output print
    elif age <= 0:
      print('too young')

  #output print then break
  else:
    print('please only put numbers')
    exit()
  break

print('oh, so you\'re ' + name + ' and you\'re ' + str(age) + ' years old')
