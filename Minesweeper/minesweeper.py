#minesweeper test
import random,pygame




class NewBoard:

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.grid = []

        
        for i in range(0,cols):
            rowsArray = []
            for j in range(0, rows):
                rowsArray.append(0)       # origin is in the top left corner    self.grid[y][x]
            
            self.grid.append(rowsArray)

    def placeMines(self, difficulty):
        numberOfMines = (board.cols * board.rows * difficulty) // 10

        for i in range(numberOfMines):
            x = random.randint(0,self.cols-1)
            y = random.randint(0,self.rows-1)

            if self.grid[x][y] != -1:
                self.grid[x][y] = -1  #  -1 is a mine

            else:
                numberOfMines += 1



        for i in range(0,self.cols):
            for j in range(0, self.rows):

                if self.grid[i][j] != -1:    
                    mineCount = 0
                    
                    for k in range(-1,2):
                        for l in range(-1,2):

                            try:
                                if i+k >= 0 and j+l >= 0 and self.grid[i+k][j+l] == -1:
                                    mineCount += 1
                            
                            except IndexError:
                                pass
                            
                                
                    self.grid[i][j] = mineCount



difficulty = 2  # 0 - 3

board = NewBoard(10,10)   #  (rows,cols) 
board.placeMines(difficulty)


for i in range(len(board.grid)):
    print(board.grid[i])






# pygame 
pygame.init()
screen = pygame.display.set_mode(((board.cols + 1) * 25, (board.rows+3) * 25 + 13))   #50 for ui at top  + 12.5 for each border


# screen
pygame.display.set_caption("Minesweeper")
icon = pygame.image.load("Minesweeper\Assets\icon.png")
pygame.display.set_icon(icon)

# colours
dGrey = (123,123,123) # 7b
grey  = (219,219,219) # db
white = (255,255,255) # ff

# pygame loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)

    # Game Box
    pygame.draw.line(screen, dGrey,(12.5,75),((board.cols + 1) * 25 - 12.5,75),2)
    pygame.draw.line(screen, dGrey,(12.5,(board.rows + 1) * 25 + 50),((board.cols + 1) * 25 - 12.5,(board.rows + 1) * 25 + 50),2)
    pygame.draw.line(screen, dGrey,(12.5,75),(12.5,(board.rows + 1) * 25 + 50),2)
    pygame.draw.line(screen, dGrey,((board.cols + 1) * 25 - 12.5,75),((board.cols + 1) * 25 - 12.5,(board.rows + 1) * 25 + 50),2)
    # UI Box
    pygame.draw.line(screen, dGrey,(12.5,12.5),((board.cols + 1) * 25 - 12.5,12.5),2)
    pygame.draw.line(screen, dGrey,(12.5,62.5),((board.cols + 1) * 25 - 12.5,62.5),2)
    pygame.draw.line(screen, dGrey,(12.5,12.5),(12.5,62.5),2)
    pygame.draw.line(screen, dGrey,((board.cols + 1) * 25 - 12.5,12.5),((board.cols + 1) * 25 - 12.5,62.5),2)
    # Game Grid
    for i in range(1,board.cols):
        pygame.draw.line(screen, dGrey,(12.5 + i*25, 75),(12.5 + i*25, (board.rows + 1) * 25 + 50),2)
        pygame.draw.line(screen, dGrey,(12.5, 75 + i*25),((board.cols) * 25 + 12.5, 75 + i*25),2)


    pygame.display.flip()
    #pygame.display.update()


