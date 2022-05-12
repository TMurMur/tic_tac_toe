# Tic Tac Toe game

import random

def drawBoard(board):
    # This function prints the game field to the screen

    # "board" - the list from 10 strings, in order to draw the game field 
    # (0 is ignored)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Accept for player to enter the letter, that he wants to use
    # Returns the list in which the player's letter - the first element and 
    # computer's one - the second
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print("What will you chose? 'X' or 'O'?")
        letter = input().upper()

    # The first element - player's letter; the second - computer's one
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # The random player's choice, who goes first
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Taking into accaunt field filling and player's letter, this function
    # returns True, if player has won
    # 'bo' - for 'board'; 'le' - for 'letter'
    return((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the center
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # to the bottom at left
        (bo[8] == le and bo[5] == le and bo[2] == le) or # to the bottom at center
        (bo[9] == le and bo[6] == le and bo[3] == le) or # across the center
        (bo[7] == le and bo[5] == le and bo[3] == le) or # across the diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # across the diagonal

def getBoardCopy(board):
    # Makes the game field copy and returns it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Returns True if step has been made into the empty cell
    return board[move] == ' '

def getPlayerMove(board):
    # Allowing a player to make a move
    move = ' '
    cells = '1 2 3 4 5 6 7 8 9'.split()
    while move not in cells or not isSpaceFree(board, int(move)):
        print("What will be your next step? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns possible move, taking into account the list of steps that have
    # been made and list of filled cells
    # Returns None if there aren't possible moves
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Taking into account the field filling and computer's letter, determines 
    # the possible move and returns it
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # This is the algorithm for Tic Tac Toe AI:
    # Firstly check wether we've won, making the next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Check wether the player has won in case of next move. Block him
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners if there are free ones
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center if it is free
    if isSpaceFree(board, 5):
        return 5

    # Make a move by one side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Returns True, if cell isn't free. In other case, returns False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("***********************\n*** > Tic Tac Toe < ***\n"
    "***********************")

while True:
    # Reload the game field
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(' ' + turn + ' makes the first move.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player':
            # The human's move
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("You're won!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("DRAW..")
                    break
                else:
                    turn = 'Computer'

        else:
            # The computer's move
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("Computer has won! You're lose!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("DRAW..")
                    break
                else:
                    turn = 'Player'

    print("Wanna play once more? (Yes/No)")
    if not input().lower().startswith('y'):
        break
