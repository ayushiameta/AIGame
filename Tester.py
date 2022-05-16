from Solver import MainSolver
import sys
import Board

"""
Execution starts from Tester.py
Example : python3 Tester.py  1 MM
functionalities:
1. Calls Board.py to generate Game Board
2. Calls Solver.py for Search Algorithms
3. generate GeneratedReadme.txt file

Final Readmefile.txt includes the output of all grid sizes : 6x6, 7x6, 8x7, 8x8
"""


def Generate_ReadmeFile():

  with open("Readme.txt", "w") as FileOpenReadme:
    if (SearchAlgorithm == "MM"):
      FileOpenReadme.write("\n **** Search Method : Minmax Algorithm **** \n")
    else:
      FileOpenReadme.write("\n **** Search Method : Minmax Algorithm with Alpha-Beta pruning **** \n")
    FileOpenReadme.write("\n Utility Function : : Empty spaces on the grid (Normalized on scale -100 to +100)\n")
    FileOpenReadme.write("\n When AI is 1st player : +1 x ((Number of Empty moves)*100)//(Row * column) \n")
    FileOpenReadme.write("\n When AI is 2nd  player : -1 x ((Number of Empty moves)*100)//(Row * column) \n\n")
    FileOpenReadme.write("\n Depth Limited Minimax with Maximum depth = 3  \n")
    FileOpenReadme.write(Board.ReadmeOutputString)


if __name__ == "__main__":

  # Defult arguments
  Player_AI = 1
  SearchAlgorithm = "MM"


  try:
    if (len(sys.argv) == 1):
      # Defult arguments
      Player_AI = 1
      SearchAlgorithm = "MM"

    else:
      Player_AI = int(sys.argv[1])
      SearchAlgorithm = sys.argv[2]

  except:

    print("In valid Arguments ")
    print("Example : python3 Tester.py  1 MM ")
    sys.exit(1)
  print("\n****************************  Grid Size "+str(Board.ROW) + "x" + str(Board.COL) + " ******************************")
  Board.ReadmeOutputString += "\n****************************  Grid Size "+str(Board.ROW) + "x" + str(Board.COL) + " ******************************\n"
  printSring = "\n**** Search Method : " + SearchAlgorithm + " ****\n"
  if(SearchAlgorithm == "MM"):
    print("\n **** Search Method : Minmax Algorithm **** \n")
  else:
    print("\n **** Search Method : Minmax Algorithm with Alpha-Beta pruning **** \n")


  Board.EmptyBoardGeneration()
  MainSolver(Player_AI, SearchAlgorithm)

  Generate_ReadmeFile()





