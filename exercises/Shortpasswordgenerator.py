import random

lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
miscchar = ["@","!","#","$","%","&","*","?"]

running = True

name = input("What is your name? ")
print("\nWelcome to the Advanced Password Generator, " + name)


def passwordgenerate(lenght):

    lenght = int(lenght)
    password = ""  # Start with empty string
    for i in range(lenght):  # Loop 4 times
            letter = random.choice(lowercase)
            password = password + letter  # Add each letter to the password
    print("Your new password is: '" + password + "' !")
    print("Thank you for using the advanced password generator.")

while running:
    print(" -- MENU -- ")
    print(" [1] Create a new password")
    print(" [2] Change your password")
    print(" [3] Quit")
    choice = input("Please enter your choice:")
    if choice == "1":
        lenght = int(input("How long would you like the password to be? Min lenght 4, Max lenght: 10, numbers only: "))
        allowmisc = input("Do you allow misc characters? (Y/N): ")
        passwordgenerate(lenght)

