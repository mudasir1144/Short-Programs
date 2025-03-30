import random
number = random.randint(1 , 10)
''''
user = int(input("Enter a number between 1 and 10: "))
if number == user:
    print("You guessed it right!")
else:
    print(f"Wrong guess! The correct number was {number}.")'
'''

for i in range(3):
    user = int(input("Enter a number between 1 and 10:"))
    if number== user:
        print("You guessed that right!")
    else:
        print(f"Wrong guess! The correst answer is {number}.")

if number !=user:
    print("You have used all the attempts")
    print(f"The correct answer is {number}.")