from mimetypes import guess_all_extensions, guess_extension

import random

print("*******************************")
print("Welcome to Python Ramdom number")
print("*******************************")

rand_number = random.random() * 100 
secret_number = int(rand_number)
tries_total = 5
turns = 1

for turns in range ( 1, tries_total+1):

    print ("Try {} of {}".format(turns,tries_total))
    guess = input("Enter a number: ")
    print ("You entered", guess )
    guess = int(guess) ##convert string to int

    correct = guess == secret_number
    greater = guess > secret_number
    less    = guess < secret_number

    if guess <= 0:
       print ("Must be greater than 0") 
       continue
     
    if (correct):
        print ("Right number!")
        break
    else:
        if(greater):
            print ("Wrong! Your guess was greater than the secret number.")
        elif(less):
            print ("Wrong! Your guess was less than the secret number." )

print ("The secret number was: {}".format(secret_number))    
print ("End game")