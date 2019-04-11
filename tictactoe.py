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

def isSpaceFree(board, move):
    #returns true if the passed move is is free on the board that is passed
    return board[move] == ''

def getComputerMove(board, computerLetter):
    #intakes a board and letter to determine and return makeMove
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #algorithm for tictactoe AI
    #see if can win in next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter)
                return i

    #Check if the player could win on thier next move, if so block themself.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter)
                return i

    #implement strategy of taking a corner if it's free
    boardCorners = [1,3,7,9]
    move = chooseRandomMoveFromList(board, boardCorners)
    ifmove != None:
        return move

    #take center if free
    if isSpaceFree(board, 5):
        return 5

    #move on a middle side
    sideMoves = [2,4,6,8]
    return chooseRandomMoveFromList(board, sideMoves)

def playAgain():
    #determines if the player would like to play again by retruning True
    print('Do you want to play again? type "y" or "n"')
    return input().lower().startwith('y')

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

    else:
        #computer's turn
        move = getComputerMove(board, computerLetter)
        makeMove(board,computerLetter, move)

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
                 turn = 'player'

    if not playAgain():
        break
