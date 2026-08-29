import random
name = input("Enter your name\n")
print(f"Welcome to the game {name}")
computer_score = 0
name_score = 0
def game():
    for i in range(0,3):
        global computer_score,name_score
        print("Before Proceeding with the game , Kindly follow some instructions")
        print("This gane consist of only 3 rounds per chance")
        print("If Computer chooses 1 then it means Snake\nIf 2 then Water\nIf 3 then Gun")
        print("Press 1 to choose Snake\nPress 2 to choose Water\nPress 3 to choose Gun")
        ch = input("Enter your choice\n")
        print(f"You Chooses : {ch}")
        L = ["Snake","Water","Gun"]
        a = random.choice(L)
        print(f"Computer Chooses : {a}")
        if (ch == "1" and a == "Snake"):
            print(f"Sorry {name} It's an Draw !!")
        elif (ch == "2" and a == "Water"):
            print(f"Sorry {name} It's an Draw !!")
        elif (ch == "3" and a == "Gun"):
            print(f"Sorry {name} It's an Draw !!")
        elif (ch == "1" and a == "Water"):
            print(f"Congratulations {name} You won because Snake beats Water")
            name_score +=1
        elif (ch == "1" and a == "Gun"):
            print(f"Sorry {name} You lose because Gun beats snake")
            computer_score +=1
        elif (ch == "2" and a == "Gun"):
            print(f"Congratulations {name} You Won because Water beats Gun")
            name_score +=1
        elif (ch == "2" and a == "Snake"):
            print(f"Sorry {name} You lose because Snake beats Water")
            computer_score +=1
        elif (ch == "3" and a == "Snake"):
            print(f"Congratulations {name} You Won because Gun beats Snake")
            name_score +=1
        elif (ch == "3" and a == "Water"):
            print(f"Sorry {name} You lose because Water beats Gun")
            computer_score +=1
    if (name_score > computer_score):
        print(f"You Won , Your score = {name_score}\n& Computer Score = {computer_score}")
    elif(name_score == computer_score):
        print(f"OMG !! {name} It's an Draw , Good Luck Ahhh")
    elif(name_score < computer_score):
        print(f"You Lose because Your Score = {name_score}\n& Computer Score = {computer_score}")
game()

while(True):
    z1 = int(input("Press 1 to continue and 0 to exit\n"))
    if (z1 == 1):
        computer_score = 0
        name_score = 0
        game()
    elif (z1 == 0):
        print("Thanks for playing the Game\nDeveloped by Aviral Tyagi")
        break
    else:
        print("Please enter the value from the options mentioned above\n")
        print("Thanks for playing the Game\nDeveloped by Aviral Tyagi")
        break

         
