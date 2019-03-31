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

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def makeMove(board, letter, move):
    board[move] = letter

print("Let's play tic-tac-toe")
#create empty board
board=['']*10
makeBoard(board)
turn = determineFirstPlayer()
print('The ' + turn + ' will go first.')
gameIsPlaying= True
while gameIsPlaying:
    if turn == 'player':
        makeBoard(board)
        move = getPlayerMove(theBoard)
        makeMove(theBoard, playerLetter, move)

         if isWinner(theBoard, playerLetter):
             drawBoard(theBoard)
