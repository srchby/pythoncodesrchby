from Classes import User, Item

p1 = User("Daniel", 12000, [])

items = [Item(0,"White t-shirt", 60), Item(1,"Purse", 120),
Item(2,"Adidas Tenis", 120),
Item(3,"Jeans Pants", 60)
        ]

def main_menu(p1):
  print(f"\nWelcome the shop {p1.name}, please select a action")
  print("\n1. Bank Account \n2. Shopping List \n3. Shop \n4. Exit")
  while True:
    user_answer = input("\n")
    if user_answer == "1":
      bank_acc(p1)
      break
    if user_answer == "2": 
      break
    if user_answer == "3":
      shop(p1)
      break
    if user_answer == "4":
      break
    else:
      print('\nInvalid Input')
      break
    
    
def bank_acc(p1):
  print(f"\nWelcome {p1.name}, please select a action:")
  print("\n1. See Bank Account \n2. Return \n3. Exit")
  while True:
    user_answer = input("\n")
    if user_answer == "1":
      print(f"Your bank account total is {p1.money}")
    if user_answer == "2": 
      main_menu(p1)
      break
    if user_answer == "3":
      print("\nThank you for your time!")
      break
    else:
      print('\nInvalid Input')
      break

def shop(p1):
  print("\nPlease select a item to buy:")
  for item in items:
    print(f"{item.id} {item.name_obj} {item.price}")

  while True:
    id = input("Select item: ")
  if id.isdigit():
    id = int(id)
  else:
    print("Error")
  print("please input a digit")
  exit()

  for item in items:
    if id == item.id:
      pass
      print(f"{item.name_obj} was added to the cart")

main_menu(p1)