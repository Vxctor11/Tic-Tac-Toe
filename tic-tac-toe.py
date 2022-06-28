#-----Create Board--------#
import random
 
print("Walcome to Tic-Tac-Toe!")

def ShowBoard(board):

  print(board[0] + "|" +board[1] + "|" + board[2] + "\n" +
  "-----\n" +
  board[3] + "|" + board[4] + "|" + board[5] + "\n" +
  "-----\n" +
  board[6] + "|" + board[7] + "|" + board[8] + "\n")
#---------------------------------------------------#
#-----Player Input--------#
def PlayerInput(board):
  Playermove = int(input("Player, where do you want to play between 1 and 9? "))
  board[Playermove -1] = "X"
  
#---------------------------------------------------#
#-----------AI Move----------------#
def AI(board):
  while True:
    move = random.randint(0,8)
    if board[move] != "X":
      board[move] = "0"
      break
#---------------------------------------------------#
#-----------Check Win----------------#
def CheckWin(board):
  #--------Horizontal------------#
  if board[0] == board[1] == board[2] == "X":
    print("Player wins!")
    return True
  elif board[3] == board[4] == board[5] == "X":
    print("Player wins!")
    return True
  elif board[6] == board[7] == board[8] == "X":
    print("Player wins!")
    return True

  if board[0] == board[1] == board[2] == "0":
    print("Computer wins!")
    return True
  elif board[3] == board[4] == board[5] == "0":
    print("Computer wins!")
    return True
  elif board[6] == board[7] == board[8] == "0":
    print("Computer wins!")
    return True
#-----------------------------------------------#
#--------Vertical------------#
  if board[0] == board[3] == board[6] == "X":
    print("Player wins!")
    return True
  elif board[1] == board[4] == board[7] == "X":
    print("Player wins!")
    return True
  elif board[2] == board[5] == board[8] == "X":
    print("Player wins!")
    return True

  if board[0] == board[3] == board[6] == "0":
    print("Computer wins!")
    return True
  elif board[1] == board[4] == board[7] == "0":
    print("Computer wins!")
    return True
  elif board[2] == board[5] == board[8] == "0":
    print("Computer wins!")
    return True
#-----------------------------------------------#
#--------Diagonal------------#
  if board[0] == board[4] == board[8] == "X":
    print("Player wins!")
    return True
  elif board[2] == board[4] == board[6] == "X":
    print("Player wins!")
    return True

  if board[0] == board[4] == board[8] == "0":
    print("Computer wins!")
    return True
  elif board[2] == board[4] == board[6] == "0":
    print("Ccomputer wins!")
    return True
#---------------------------------------------------#
#  #----------------Tie----------------------#

#---------------------------------------------------#
#--------------------Game Loops-----------------------#
def main():
  game = True
  board = ['1','2','3','4','5','6','7','8','9']
  while game:
    ShowBoard(board)
    PlayerInput(board)
    AI(board)
    if CheckWin(board):
      ShowBoard(board)
      game = False
      break
#---------------------------------------------------#
main()