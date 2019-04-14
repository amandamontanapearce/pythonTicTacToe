#!/usr/bin/python

#tic tac toe
import random

def makeBoard(board):
    # prints board that was passed to it
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])


def inputPlayerLetter():
    l=''
    while not(l=='X' or l=='O'):
        l=raw_input("Do you want to be X or O?").upper()
    if l=='X':
        return ['X','O']
    else:
        return ['O','X']

def determineFirstPlayer():
    #randomly choose player or computer
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def getBoardCopy(board):
    dupBoad = []
    for i in board:
        dupBoad.append(i)
    return dupBoad

def isBoardFull(board):
    #returns true if every space is taken
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = raw_input('What is your next move? (1-9)')
    return int(move)

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    # checks all possible win combos and returns True if the player has won
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal top left/bottom right
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal top right/bottom left

def isSpaceFree(board, move):
    #returns true if the passed move is is free on the board that is passed
    return board[move] == ''

def chooseRandomMoveFromList(board, moveList):
    #returns move from list if valid or returns none
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

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
            if isWinner(copy, computerLetter):
                return i

    #Check if the player could win on thier next move, if so block themself.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #implement strategy of taking a corner if it's free
    boardCorners = [1,3,7,9]
    move = chooseRandomMoveFromList(board, boardCorners)
    if move != None:
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

while True:
    #reset the board
    board=['']*10
    playerLetter,computerLetter = inputPlayerLetter()
    turn = determineFirstPlayer()
    print('The ' + turn + ' will go first.')
    gameIsPlaying= True

    while gameIsPlaying:
        if turn == 'player':
            makeBoard(board)
            move = getPlayerMove(board)
            makeMove(board, playerLetter, move)

            if isWinner(board, playerLetter):
                makeBoard(board)
                print('You Won!')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    makeBoard(board)
                    print('Cats game! You tied')
                    break
                else:
                    turn = 'computer'
        else:
            #computer's turn
            move = getComputerMove(board, computerLetter)
            makeMove(board,computerLetter, move)

            if isWinner(board, playerLetter):
                makeBoard(board)
                print('You Won!')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    makeBoard(board)
                    print('Cats game! You tied')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
