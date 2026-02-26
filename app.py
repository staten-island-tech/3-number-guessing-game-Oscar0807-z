import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = random.choice(my_list)
number = input("Guess a random number between 1-10")

""" if int(number) != random_number:
    print ("Incorrect")
    print (number)
    x = input("Try again")
if int(x) != random_number:
    print ("Incorrect")
    print (x) and (number)
    y = input("Try again2")
if int(y) != random_number: 
    print ("Incorrect") 
    print (y) and (x) and (number)
    z = input("Try again3") """


history = []
while int(number) != random_number:
    print ("Incorrect")
    history.append(number)
    print (number)
    if int(number) > random_number:
        print ("Too high")
    if int(number) < random_number:
        print ("Too low")
    number = input("Try again")
    print (history)
    
else:
    print ("Correct") 
for x in history:
    print (x)
