
"""
This file implements all board related functions
Initial Board size 6x6
1. Board initialization
2. Checking Next move
3. Board Print
4. Validity of move
5. Utility function

"""

import Board

#initial Board
GameBoard = {}
ROW = 6
COL = 6
ReadmeOutputString = " "

def UtilityFunction( board ):
    #utility function
    #((Number of Empty moves) * 100) // (Row * column)
    NumberOfEmptyMoves = 0
    for pos in board.keys():
        if board[pos] == '-':
            NumberOfEmptyMoves += 1
    return ((NumberOfEmptyMoves)*100)//(ROW*COL)





def EmptyBoardGeneration():
    # Creating a board
    for row in range(1, ROW + 1):
        for col in range(1, COL + 1):
            GameBoard[f'{row}/{col}'] = '-'
    return


BOARD_B = GameBoard.copy()



def BoardGenerationAfterEveryMove():

    String_ReadMeOutput = ""
    Copied_Board = GameBoard.copy()
    String_ReadMeOutput = first_upper_line(String_ReadMeOutput)
    String_ReadMeOutput = second_line(String_ReadMeOutput)

    for row in range(1, ROW + 1):
        print(row, end=' ')
        String_ReadMeOutput += str(row)
        for col in range(1, COL + 1):
            print('|', Copied_Board[f'{row}/{col}'], '', end='')
            String_ReadMeOutput += ' | ' + Copied_Board[f'{row}/{col}']


        print('|')
        String_ReadMeOutput += ' | ' +'\n'

        print('  ', end='')
        String_ReadMeOutput +='  '
        print('----' * COL, end='')
        String_ReadMeOutput += ('----' * COL)
        print('\n')
        String_ReadMeOutput += '\n'
    Board.ReadmeOutputString += String_ReadMeOutput

    print('')



def checkForMove():
    for pos in GameBoard.keys():
        if GameBoard[pos] == '-':
            return True
    else:
        return False


def player_Move_Insertion(PlayerLetter, PlayerMove):
    if CheckEmptySpace(PlayerLetter, PlayerMove):
        if PlayerMove:
            GameBoard[PlayerMove] = PlayerLetter
            applyMove(PlayerMove)
    else:
        return



def second_line(outputString):
    print('  ', end='')
    outputString += '  '
    print('----' * COL, end='')
    outputString += ('----' * COL)
    print('-')
    outputString += "-\n"
    return outputString


def first_upper_line(outputString):
    print(' ' * 3, end='')
    outputString += "\n" + ' ' * 3
    for i in range(1, COL + 1):
        print(f'{i}   ', end='')
        outputString += f'{i}' + "   "
    print(end='\n')
    outputString += "\n"
    return outputString


def CheckEmptySpace(letter, playerMove):
    global Move
    if playerMove in GameBoard.keys():
        if GameBoard[playerMove] == "-":
            return True
        else:
            print("Invalid Insert")
            playerMove = input('Please enter new position : ')
            player_Move_Insertion(letter, playerMove)
    else:
        print('Invalid Insert')
        playerMove = input('Please Enter new position : ')
        player_Move_Insertion(letter, playerMove)
    return False


def applyMove(position):
    position = position.split('/')
    row = int(position[0])
    col = int(position[1])
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r == row and c == col:
                continue
            else:
                if f'{r}/{c}' in GameBoard.keys():
                    GameBoard[f'{r}/{c}'] = '/'
                else:
                    continue



