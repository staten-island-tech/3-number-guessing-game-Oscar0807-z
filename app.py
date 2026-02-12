""" numbers = [1,2,3,4,5,6,7,8,9,10] 
(number) = input("Guess a number between 1-10")
random_item = (number)

while (number) > 2:
    print ("The number should be lower")

while number < 2:
    print ("The number should be higher")

while number == 2:
    print("Correct")

print (number) """
import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = random.choice(my_list)
(number) = input("Guess a random number between 1-10")
while number != random_number:
    print ("Incorrect")
    print (number)
    break 
if number < random_number:
    print ("Your number should be higher")

if number > random_number:
    print ("Your number should be lower")
