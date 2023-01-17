import random

guesstakes= 0
print("Hello whats your name? ")
myname = input()
number = random.randint(0, 20)
print('Well hello '+ myname + ' Im thinking of a number 1 thru 20.')

while guesstakes < 10:
     print(" please take a guess")
     guess = input()
     guess = int(guess)

     guesstakes = guesstakes + 1

     if guess < number:
         print("higher!")

     if guess > number:
         print("lower!")

     if guess == number:
          break

if guess == number:
     guesstakes = str(guesstakes)
     print("great job "+ myname + "! you got it in " +guesstakes+ " guesses!")

if guess != number:
     number= str(number)
     print("Nope! The number i was thinking was "+ number)

