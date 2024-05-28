# https://www.youtube.com/watch?v=8lhxIOAfDss

def factorial(n):
  if n == 1: 
    return 1
  else:
    return n * factorial(n-1)

print(factorial(4))

# /////////////////////////////////////

def move(f,t):
  print("move block {} to {}".format(f,t))

def move_block(n,f,h,t):
  #n - number of disks
  #f - from position
  #h - helper position
  #t - target position
  if n == 0:
    pass
  else:
    move_block(n-1,f,t,h)
    move(f,t)
    move_block(n-1,h,f,t)

# /////////////////////////////////////

