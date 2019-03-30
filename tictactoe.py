#tic tac toe
import random

def makeBoard(board):
    # prints board that was passed to it
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])

def determineFirstPlayer():
    #randomly choose player or computer
    if random.radient(0,1)==0:
        return 'computer'
    else:
        return 'player'


print("Let's play tic-tac-toe")
#create empty board
board=['']*10
makeBoard(board)
turn = determineFirstPlayer()
print('The ' + turn + ' will go first.')
