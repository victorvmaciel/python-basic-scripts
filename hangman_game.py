
def play_game():
    print("*******************************")
    print(*"Welcome to Python Hangman game")
    print("*******************************")

    secret_word = "banana"
    secret_word = secret_word.strip()
    hanged = False
    answer_right = False

    while (not hanged and not answer_right ):

        guess = input("Which letter? ")
        
        index = 0
        for letter in secret_word:
            if (guess.upper == letter.upper ):
                print( "Letter '{}' found on position '{}' ".format(guess.index,index))
            index = index + 1

        
        print ("Keep playing...")
        
    if (secret_word.find == True):
      print(*"End game")

if (__name__ == "__main__"):
    play_game()