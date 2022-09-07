
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over
import random

n=random.randint(1,20)
# print(n)
numberOFGuesses=1
print("Number of guesses is limited to only 9 times: ")
while (numberOFGuesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<n:
        print("Please input greater number.\n")
    elif guess_number>n:
        print("Please input smaller number.\n ")
    else:
        print("you won\n")
        print(numberOFGuesses,"no.of guesses he took to finish.")
        break
    print(9-numberOFGuesses,"no. of guesses left")
    numberOFGuesses = numberOFGuesses + 1

if(numberOFGuesses>9):
    print("Game Over")
  
