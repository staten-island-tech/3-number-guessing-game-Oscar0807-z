import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = random.choice(my_list)
number = input("Guess a random number between 1-10")
while int(number) != random_number:
    print ("Incorrect")
    print (number)
    input("Try again")
    
if ("Try again") == random_number:
    print ("Correct")
if int(number) < random_number:
    print ("Your number should be higher")
if int(number) > random_number:
    print ("Your number should be lower")
