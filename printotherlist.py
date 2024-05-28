list1 = ['a', 'b', 'c']

n = 1

while n < 10:
  for i in list1:
    if i == 'c':
      n += 1
      continue

    print(i)
