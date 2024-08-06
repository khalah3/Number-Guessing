import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number=int(random.choice(range(1,101)))
print(number)
print("Choose a difficulty level, easy or hard")
difficulty_level=input()
if difficulty_level=="easy":
  attempts=10
elif difficulty_level=="hard":
  attempts=5

while attempts!=0:
  print("Make a guess")
  guess=int(input()) 
  if guess > number:
    print("Too High")
    attempts=attempts-1
    print(f"You have {attempts} attempts remaining to guess the number\n")
  elif guess < number:
    print("Too Low")
    attempts=attempts-1
    print(f"You have {attempts} attempts remaining to guess the number\n")
 
  elif guess==number:
    print("You made the right guess")
    attempts=0
  else:
    print("You ran out of attempts")
      
    

  
      
      
