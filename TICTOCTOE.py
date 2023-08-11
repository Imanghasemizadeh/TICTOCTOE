print("in the name of Allah")
# TICTOKTOE game by iman
from pyfiglet import Figlet

def show(): 
    for row in game_board:
        print(row)
    for cell in row:
        print(cell, end= " ")
    print()   

def checkforwin1():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("Player1 Won!")
def checkforwin2():
    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("Player1 Won!")
def checkforwin3():
    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("Player1 Won!")
def checkforwin4():
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("Player1 Won!")

def checkforwin5():
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("Player1 Won!")

def checkforwin6():
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("Player1 Won!")

def checkforwin7():
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("Player1 Won!")

def checkforwin8():
    if game_board[2][0] == "X" and game_board[1][1] == "X" and game_board[0][2] == "X":
        print("Player1 Won!")

def checkforwin9():
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("Player2 Won!")

def checkforwin10():
    if game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("Player2 Won!")

def checkforwin11():
    if game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("Player2 Won!")

def checkforwin12():
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("Player2 Won!")

def checkforwin13():
    if game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("Player2 Won!")

def checkforwin14():
    if game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("Player2 Won!")

def checkforwin15():
    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("Player2 Won!")

def checkforwin16():
   if game_board[2][0] == "O" and game_board[1][1] == "O" and game_board[0][2] == "O":
        print("Player2 Won!") 

def fordraw():
    if game_board[0][0] != "_" and game_board[0][1] != "_" and game_board[0][2] != "_" and game_board[1][0] != "_" and game_board[1][1] != "_" and game_board[1][2] != "_" and game_board[2][0] != "_" and game_board[2][1] != "_" and game_board[2][2] != "_":
        print("No One wins.")

f = Figlet(font='slant')
print(f.renderText('Welcome to Tic Tac Toe'))

game_board = [["_" , "_" , "_"],
              ["_" , "_" , "_"],
              ["_" , "_" , "_"]]
show()

#player1
while True:
    print("player1")
    while True:
        row = int(input("enter row: "))
        col = int(input("enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "_":
                game_board[row][col] = "X"
                show()
                checkforwin1()
                checkforwin2()
                checkforwin3()
                checkforwin4()
                checkforwin5()
                checkforwin6()
                checkforwin7()
                checkforwin8()
                fordraw()
                break
            else:
                print("Choose another one!")
        else:
            print("Wrong number! choose 0 or 1 or 2.")
#player2
    print("player2")
    while True:
        row = int(input("enter row: "))
        col = int(input("enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "_":
                game_board[row][col] = "O"
                show()
                checkforwin9()
                checkforwin10()
                checkforwin11()
                checkforwin12()
                checkforwin13()
                checkforwin14()
                checkforwin15()
                checkforwin16()
                fordraw()
                break
            else:
                print("Choose another one!")
        else:
            print("Wrong number! choose 0 or 1 or 2.")