import random
def game_win(comp,user):
    if comp == user:
        return None
    elif comp == "r":
        if user == "p":
            return True
        elif user == "s":
            return False
    elif comp == "p":
        if user == "s":
            return True
        elif user == "r":
            return False
    elif comp == "s":
        if user == "p":
            return True
        elif user == "r":
            return False
       
computer = print("Computer Turn : rock(r), paper(p), scissor(s) ")
randNo = random.randint(1,3)
if randNo == 1:
  computer = "r"
elif randNo == 2:
  computer = "p"
elif randNo == 3:
  computer = "s"
you = input("Your Turn : Please Choose any one Rock(r), Paper(p), scissor(s) : ")  

print(f"Computer Chooses {computer}")
print(f"Player Chooses {you}")
win_loss = game_win(computer,you)
if win_loss == None:
    print("Match Draw")
elif win_loss == True:
    print("Congrats You Win the Match")
elif win_loss == False:
    print("You Loosed The Match")