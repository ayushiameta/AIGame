import Board

"""
Implemented Depth limited Minimax and Minimax with AlphaBeta Pruning
functionalities:
1. Minimax Algorithm
2. Minimax Algorithm with Alpha Beta Pruning
"""



firstPlayer = 'O'
secondPlayer = 'X'


def MainSolver(AIplayer, Algo):

    InitializePlayer(AIplayer)

    while (1):
        if(AIplayer == 1):
            if(Board.checkForMove()):
                AIPlayerMove(firstPlayer, Algo)
            else:
                print("Human Player won")
                Board.ReadmeOutputString += "Human Player won"
                break

            if (Board.checkForMove()):
                HumanplayerMove(secondPlayer)
            else:
                print("AI player won ")
                Board.ReadmeOutputString += "AI Player won"
                break

        else:
            if (Board.checkForMove()):
                HumanplayerMove(firstPlayer)
            else:
                print("AI player won ")
                Board.ReadmeOutputString += "AI Player won"
                break

            if (Board.checkForMove()):
                AIPlayerMove(secondPlayer, Algo)
            else:
                print("Human Player won")
                Board.ReadmeOutputString += "Human Player won"
                break


def minimax(board, treeDepth, MaxPlayer, PlayerLetter, DepthLevel):

    if( Board.checkForMove() == False):
        if(MaxPlayer):
            return 100
        else:
            return -100

    if (treeDepth >= 4):
        if(MaxPlayer):
            # Calling Utility Function
            # Multiplying with +1 if AI is max player
            return 1* Board.UtilityFunction(board)
        else:
            # Calling Utility Function
            # Multiplying with -1 if AI is min player
            return -1 * Board.UtilityFunction(board)
    DepthLevel[treeDepth] = DepthLevel[treeDepth] + 1

    if MaxPlayer:
        bestScore = -200
        for key in Board.GameBoard.keys():
            if (Board.GameBoard[key] == '-'):
                BOARD_cpy = Board.GameBoard.copy()
                Board.player_Move_Insertion(PlayerLetter, key)
                score = minimax(Board.GameBoard, treeDepth + 1, False, PlayerLetter, DepthLevel)
                Board.GameBoard  = BOARD_cpy.copy()
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 200
        for key in Board.GameBoard.keys():
            if (Board.GameBoard[key] == '-'):
                BOARD_cpy = Board.GameBoard.copy()
                Board.player_Move_Insertion(PlayerLetter, key)
                score = minimax(Board.GameBoard, treeDepth + 1, True, PlayerLetter, DepthLevel)
                Board.GameBoard = BOARD_cpy.copy()
                if (score < bestScore):
                    bestScore = score
        return bestScore

def MiniMaxWithAlphaBetaPruning(board, treeDepth, MaxPlayer, PlayerLetter, alpha, beta, DepthLevel):
    if( Board.checkForMove() == False):
        if(MaxPlayer):
            return 100
        else:
            return -100
    if (treeDepth >= 4):
        if(MaxPlayer):
            #Calling Utility Function
            #Multiplying with +1 if AI is max player
            return 1 * Board.UtilityFunction(board)
        else:
            # Calling Utility Function
            # Multiplying with -1 if AI is min player
            return -1 * Board.UtilityFunction(board)
    DepthLevel[treeDepth] = DepthLevel[treeDepth] + 1
    if MaxPlayer:
        best_score = -101
        for key in Board.GameBoard.keys():
            if (Board.GameBoard[key] == '-'):
                board_cpy = Board.GameBoard.copy()
                Board.player_Move_Insertion(PlayerLetter, key)
                score = MiniMaxWithAlphaBetaPruning(Board.GameBoard, treeDepth + 1, False, PlayerLetter, alpha, beta, DepthLevel)
                Board.GameBoard  = board_cpy.copy()

                best_score = max(best_score, score)
                alpha = max(alpha,best_score)
                if(alpha >= beta):
                    break
        return best_score

    else:
        best_score = 101
        for key in Board.GameBoard.keys():
            if (Board.GameBoard[key] == '-'):
                board_cpy = Board.GameBoard.copy()
                Board.player_Move_Insertion(PlayerLetter, key)
                score = MiniMaxWithAlphaBetaPruning(Board.GameBoard, treeDepth + 1, True, PlayerLetter, alpha, beta, DepthLevel)
                Board.GameBoard = board_cpy.copy()
                if (score < best_score):
                    best_score = score
                beta = min(beta, best_score)
                if (alpha >= beta):
                    break
        return best_score




def HumanplayerMove(player):
    #Get Input from user
    position = input('Human Player Input: ' + player)
    Board.player_Move_Insertion(player, position)
    Board.ReadmeOutputString += "\n\n Board after Human Player Move: \n"
    Board.BoardGenerationAfterEveryMove()

def InitializePlayer(AIplayer):
    if (AIplayer == 1):
        print("Player 1: AI  ")
        print("Player 2 : Human")
        Board.ReadmeOutputString += "Player 1: AI  \n" + "Player 2 : Human\n"
    else:
        print("Player 1: Human  ")
        print("Player 2 : AI")
        Board.ReadmeOutputString += "Player 1: Human \n" + "Player 2 : AI \n"


def AIPlayerMove(PlayerSymbol, SearchAlgo):

    bestScore = -1000
    bestMove = "null"
    DepthLevel = { 1: 0, 2 : 0 , 3: 0}
    for key in Board.GameBoard.keys():
        if(Board.GameBoard[key] == '-'):
            BOARD_cpy = Board.GameBoard.copy()
            Board.player_Move_Insertion(PlayerSymbol, key)
            if(SearchAlgo == "MM"):
                score = minimax(Board.GameBoard, 1, True, PlayerSymbol, DepthLevel)
            else:
                score = MiniMaxWithAlphaBetaPruning(Board.GameBoard, 1, True, PlayerSymbol, -101, 101, DepthLevel)
            Board.GameBoard = BOARD_cpy.copy()
            if(score > bestScore):
                bestScore = score
                bestMove = key

    print("\nAI Moved at position : " + bestMove)
    Board.ReadmeOutputString += "\n\n Board after AI Moved at Position : " + str(bestMove)
    Board.player_Move_Insertion(PlayerSymbol, bestMove)
    Board.BoardGenerationAfterEveryMove()
    print("Depth :   number of nodes expanded")
    Board.ReadmeOutputString += "\n Depth :  Number of nodes expanded at given depth level\n  "

    PrintDepthLevel(DepthLevel)
    return


def PrintDepthLevel(DepthLevel):
    for key, value in DepthLevel.items():
        Board.ReadmeOutputString += str(key) + " : " + str(value) + "\n"
        print(key, ' : ', value)








