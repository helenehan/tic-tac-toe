# evaluate function

def evaluate(strt):
  if "xxx" in strt:
    return "x"
  elif "ooo" in strt:
    return "o"
  elif "-" not in strt:
    return "!"
  else: 
    return "-"


# player move funciton

def player_move(strt):
    position = int(input("What is your move? Please type in a number between 0 and 19: "))
    mark = "x"
    if -1 < position < 20 and strt[position] == "-":
        strt = strt[:position] + mark + strt[position + 1:]
        return strt
    else :
        print("Error - please try again")
        return player_move(strt)


# pc move function

from random import randrange  # (and possibly other import statements that are needed)

def pc_move(strt):
    "Returns a game board with the computer's move."
    mark = "o"
    position = randrange(0, 20)
    if strt[position] == "-":
        strt = strt[:position] + mark + strt[position + 1:]
        return strt
    else:
        return pc_move(strt)



# final tic tac toe function


strt = "--------------------"

def tic_tac_toe(strt):  
    print(strt)
    evaluate(strt)
    while evaluate(strt) == "-":
        strt = player_move(strt)
        strt = pc_move(strt)
        print(strt)
    if evaluate(strt) == "x":
        print("End Game. You won")
    elif evaluate(strt) == "o":
        print("End game. The computer has won.")
    elif evaluate(strt) == "!":
        print("End game. The board is full, nobody has won.")
        

tic_tac_toe(strt)
