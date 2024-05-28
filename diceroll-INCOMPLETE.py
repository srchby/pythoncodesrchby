import random
score = 0
rounds = 0

def dice():
  dice_num = random.randint(1, 10)
  while True:
    if dice_num in (2, 10):
      print(f"You rolled a {dice_num}")
      rounds = rounds + 1
    else:
      print(f"looks like you got a {dice_num}")
      rounds = rounds + 1

while True:
  #get user input if they want to play
  play_game = input("want to play game (Y/N): ")
  if play_game in ("Y", "y", "yes"):
    print("k")
    dice()
      
  elif play_game in ("N", "n", "no"):
    print("ok")
    quit()
      
  else:
    print("Invalid")
    break

def dice_game():
  #user input to roll dice and dice rand numb
  roll = input("Would you like to roll the dice this round? (Y/N): ")
  if roll in ("Y", "y", "yes"):
    print("k")
  elif roll in ("n", "N", "no"):
    rounds += 1
    print("okay then")
    