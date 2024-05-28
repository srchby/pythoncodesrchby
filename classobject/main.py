from user import user
users = open('user_record.txt', 'a+')

print('\nLet\'s start making your account!')

try:
  input_name = str(input('\nPlease input your name: '))
  input_age = int(input('\nPlease input your age: '))
except ValueError:
  print('Input Error')
  quit

user1 = user('\n' + input_name, input_age, input_verified)

print(user1.name)
print(user1.age)
print(user1.verified)

users.write('\n' + input_name + '\n' + str(input_age))

users.close()