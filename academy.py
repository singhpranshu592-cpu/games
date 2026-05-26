import random

def diceroll_game():

    while True :
        print("Dice Roll Game")
        print("1.Roll dice")
        print("2.Back to Main Menu")

        option = input("Enter choice: ")

        if option =="1":
            user = random.randint(1,6)
            computer = random.randint(1,6)

            print("you rolled: ",user)
            print("Computer rolled: ",computer)

            if user>computer:
                print("you won")
            elif computer>user:
                print("u lost")

        elif option=="2":
            break
        else:
            print("invalid choice")

def stone_paper_scissor():
    choices=["stone","paper","scissor"]

    while True:
        print("Stone Paper Scissor")
        print("1.Play game")
        print("2.Back to main menu")

        option = input("Enter a choice: ")

        if option=="1":
            user = input("Enter stone / paper / scissor : ").lower()

            if user not in choices:
                print("Invalid choice")
                continue

            computer = random.choice(choices)

            print("You chose: " , user)
            print("Computer chose: ", computer)

            if user == computer:
                print("Result : Match Draw!")
            elif(user == "stone" and computer =="scissors") or \
                (user == "paper" and computer =="stone") or \
                (user == "scissors" and computer =="paper"):
                print("Result: You Win!")

            else:
                print("Result: You lost!")

        elif option =="2":
            break
        else:
            print("Invalid Choice")

def main():

    while True:
        print("SIMPLE GAME MENU")
        print("1. Stone Paper Scissors")
        print("2. Dice Roll Game")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stone_paper_scissor()

        elif choice == "2":
            diceroll_game()

        elif choice == "3":
            print("Thank You for Playing!")
            break

        else:
            print("Invalid Choice!")

main()