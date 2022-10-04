#minesweeper test
import random


difficulty = 2  # 0 - 3

class NewBoard:

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.grid = []

        
        for i in range(0,cols):
            rowsArray = []
            for j in range(0, rows):
                rowsArray.append(0)       # origin is in the top left corner
            
            self.grid.append(rowsArray)

    def placeMines(self, difficulty):
        numberOfMines = (board.cols * board.rows * difficulty) // 5

        for i in range(numberOfMines):
            x = random.randint(0,self.cols-1)
            y = random.randint(0,self.rows-1)

            if self.grid[x][y] != -1:
                self.grid[x][y] = -1  #  -1 is a mine

            else:
                numberOfMines += 1





board = NewBoard(5,5)
board.placeMines(difficulty)

for i in range(5):
    print(board.grid[i])

print(board.grid[3][4])



