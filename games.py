import guess_game
import hangman_game


print("*******************************")
print("Choose your game")
print("*******************************")


print ("Press (1) for Guess Game")
print ("Press (2) fpr Hangman Game")

game_option = int(input())

if ( game_option == 1 ):
    print ("Playing Guess Game")
    guess_game.play_game()
elif ( game_option==2 ):
     print ("Playing Hangman")
     hangman_game.play_game()    
