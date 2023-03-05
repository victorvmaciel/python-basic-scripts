import random

def play_game():
    print("*******************************")
    print("Welcome to Python Ramdom number")
    print("*******************************")

    rand_number = random.randrange(1,101)
    secret_number = int(rand_number)
    tries_total = 5
    turns = 1
    scores = 1000

    print ("Random numer: {}".format(rand_number))
    print ("LEVEL ")
    print (" (1) Easy: 20 tries")
    print (" (2) Medium: 10 tries")
    print (" (3) hard: 5 tries")

    difficulty = int(input ("Choose your level: "))

    if (difficulty == 1):
        print ("You choose easy level")
        tries_total = 20
    elif (difficulty == 2):
        print ("You choose medium level")
        tries_total = 10
    else:
        print ("You choose the hard level! Good luck")
        tries_total = 5

        
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
            print ("Total of scores: {}".format(scores))
            break
        else:
            if(greater):
                print ("Wrong! Your guess was greater than the secret number.")
            elif(less):
                print ("Wrong! Your guess was less than the secret number." )

            lost_scores = abs(secret_number - guess)
            scores = abs(scores - lost_scores) - 3
            
    print ("The secret number was: {}".format(secret_number))    
    print ("End game")

if (__name__ == "__main__"):
    play_game()