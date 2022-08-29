from mimetypes import guess_all_extensions, guess_extension


print("*******************************")
print("Welcome to Python Ramdom number")
print("*******************************")

secret_number = 42
tries = 5

guess = input("Enter a number: ")

print ("You entered", guess )

guess = int(guess) ##convert string to int

if (guess == secret_number):
    print ("Right number!")
else:
    print ("Wrong number")