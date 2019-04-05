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

def isWinner(board, letter):
    # checks all possible win combos and returns True if the player has won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal top left/bottom right
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal top right/bottom left

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
        move = getPlayerMove(board)
        makeMove(board, playerLetter, move)

         if isWinner(board, playerLetter):
             drawBoard(board)
             print('You Won!')
             gameIsPlaying = False
        else:
             if isBoardFull(board):
                 drawBoard(board)
                 print('Cats game! You tied')
                 break
             else:
                 turn = 'computer'
