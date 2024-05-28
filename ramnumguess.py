import random

#defining answer, guess and the number of guesses
answer = random.randint(1,10)
guess = ''
numb_guess = 0

print('\ni\'m thinking of a number between 1 and 10')

#making the guesses five in total
for guess in range(5):

  try:
    guess = int(input('\nPlease guess a number: '))
  except ValueError:
    print('\nPlease only input numbers')

  
  #if the guess is wrong, plus one to the number of guesses and print a answer based on the number of tries
  if guess != answer:
    print('\nWrong')
    numb_guess += 1

    if numb_guess == 1:
      print('\nYou\'ve guessed ' + str(numb_guess) + ' time wrong')

    elif numb_guess in [2,3,4]:
      print('\nYou\'ve guessed ' + str(numb_guess) + ' times wrong')

    #if the number of guesses is 5, end of the game
    elif numb_guess == 5:
      print('\nYour number of guesses is over, please try again')

  #if the guess is right, plus one to the number of guesses and print a answer based on the number of tries and the right number
  elif guess == answer:
    numb_guess += 1
    print('\nCongrats')
    
    if numb_guess == 1:
      print('\nYou took only ' + str(numb_guess) + ' try to get it right, the number was ' + str(answer))
    
    else:
      print('\nYou took ' + str(numb_guess) + ' times to get it right, the answer was ' + str(answer))
    break