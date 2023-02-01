# Oliver Smith  
# Minesweeper

import random, time

class board():

    def __init__(self,rows,cols,number_of_mines,difficulty):

        self.rows = rows
        self.cols = cols
        self.number_of_mines = number_of_mines
        self.difficulty = difficulty

        self.grid = []
        self.display_grid = []


    def create_board(self): # sets up the board for play
        
        self.grid.clear()
        self.display_grid.clear()

        # Create 2d array for the grid and display_grid
        for i in range(0,self.cols):
                rows_array = []
                display_rows_array = []
                for j in range(0, self.rows):
                    rows_array.append(0)
                    display_rows_array.append(" ")
                self.grid.append(rows_array)  
                self.display_grid.append(display_rows_array)  


        # Place mines randomly on board 
        for i in range(0,self.number_of_mines):
            x = random.randint(0,self.cols-1)
            y = random.randint(0,self.rows-1)

            if self.grid[x][y] != -1:
                self.grid[x][y] = -1  #  -1 is a mine

            else:
                while self.grid[x][y] == -1:
                    x = random.randint(0,self.cols-1)
                    y = random.randint(0,self.rows-1)
                self.grid[x][y] = -1


        # Number of adjacent mines
        for i in range(0,self.cols):
                for j in range(0, self.rows):

                    if self.grid[i][j] != -1:    
                        mine_count = 0
                        
                        for k in range(-1,2):
                            for l in range(-1,2):

                                try:
                                    if i+k >= 0 and j+l >= 0 and self.grid[i+k][j+l] == -1:
                                        mine_count += 1
                                
                                except IndexError:
                                    pass
                                
                                    
                        self.grid[i][j] = mine_count



    def dfs_empty_cells(self,x,y,visited):  # Depth first search to find all adjacent empty cells

        self.display_grid[y][x] = str(self.grid[y][x]) # you said that setting the empty squares to 0 rather than leaving them blank was okay

        queue = [(x,y)]
        visited.append((x,y)) 

        for i in range(-1,2):
            for j in range(-1,2):
                current = queue[0]
                
                try:
                    if not((current[0]+i,current[1]+j) in visited) and current[0]+i >= 0 and current[1]+j >= 0 and (i,j) != (0,0) and self.grid[current[1]+j][current[0]+i] == 0: 
                        queue.append((current[0]+i,current[1]+j))

                except IndexError:
                    pass
                
        queue.pop(0) 

        for cell in queue:
            if not((cell[0],cell[1]) in visited):
                self.dfs_empty_cells(cell[0],cell[1],visited)
    
        return visited



    def game_play(self,action,x,y): # action: [1] = open  [2] = flag

        global game_over
        global game_won


        if action == 1:
            
            if self.display_grid[y][x] == "F": # Check if cell is flagged
                print("\n[This cell is flagged]")
                

            elif self.grid[y][x] == -1: # Checks if hit mine  
                game_over = True

    
            elif self.display_grid[y][x] == "0": # Check if cell is already open
                print("\n[This cell is already open]")
                

            elif self.grid[y][x] == 0:  # Check if cell is empty
                visited = self.dfs_empty_cells(x,y,[])

                # outer ring of numbers    -     wasn't sure if i had to include this in the reccursive loop but you said that i didn't need to
                for n in range(len(visited)):
                    current = visited[n]
                    for k in range(-1,2):
                        for l in range(-1,2):

                            try:
                                if current[0]+k >= 0 and current[1]+l >= 0 and (k,l) != (0,0) and self.grid[current[1]+l][current[0]+k] != 0 :
                                    self.display_grid[current[1]+l][current[0]+k] = str(self.grid[current[1]+l][current[0]+k])
                            
                            except IndexError:
                                pass

            else:
                self.display_grid[y][x] = str(self.grid[y][x]) # display the clue numbers




        elif action == 2:

            if self.display_grid[y][x] == "F": # Check if cell is flagged
                print("\n[The cell has been unflagged]")
                self.display_grid[y][x] = " "
                return

            elif self.display_grid[y][x] != " ": # Check if cell is already open
                print("\n[This cell is already open]")
                return

            else:
                self.display_grid[y][x] = "F"
                
                count = 0
                for i in range(len(self.grid)):
                        for j in range(len(self.grid[0])):
                            if self.grid[i][j] == -1 and self.display_grid[i][j] == "F":
                                count += 1
                
                if (count >= 10 and self.difficulty == 1) or (count >= 40 and self.difficulty == 2) or (count >= 99 and self.difficulty == 3): # Checks if all of the mines have been found
                    game_over = True
                    game_won = True


        elif action == 3:
            while True:
                y = random.randint(0,len(self.grid)-1)
                x = random.randint(0,len(self.grid[0])-1)
                    
                if self.grid[y][x] == -1 and self.display_grid[y][x] != "F":
                    self.display_grid[y][x] = "F"
                    count = 0
                    for i in range(len(self.grid)):
                            for j in range(len(self.grid[0])):
                                if self.grid[i][j] == -1 and self.display_grid[i][j] == "F":
                                    count += 1
                    
                    if (count >= 10 and self.difficulty == 1) or (count >= 40 and self.difficulty == 2) or (count >= 99 and self.difficulty == 3): # Checks if all of the mines have been found
                        game_over = True
                        game_won = True

                    return
                
                            

    def print_board(self): # Procedure for printing display grid

        # Prints grid and y coordinates
        for i in range(len(self.display_grid)):
            if len(self.display_grid) - (i) < 10: # to fix alignment
                print("(" + str(len(self.display_grid) - (i)) + ") ",self.display_grid[i])
            else:
                print("(" + str(len(self.display_grid) - (i)) + ")",self.display_grid[i])
            

        # Prints x coordinates
        xcoords = "     "
        for i in range(len(self.grid[0])):
            if i < 9: # to fix alignment
                xcoords += " (" + str(i+1) + ") "
            else:
                xcoords += " (" + str(i+1) + ")"
        print(xcoords)









game_over = False
game_won = False

class game():

    def __init__(self,difficulty):

        while difficulty <= 0 or difficulty > 3:

            try:
                difficulty = int(input("Choose difficulty: [1] Beginner\n                   [2] Intermediate\n                   [3] Expert\n\n>"))
                if difficulty == 1:
                    total_mines = 10
                    game_board = board(9,9,total_mines,difficulty)
                elif difficulty == 2:
                    total_mines = 40
                    game_board = board(16,16,total_mines,difficulty)
                elif difficulty == 3:
                    total_mines = 99
                    game_board = board(30,16,total_mines,difficulty)
                else:
                    print("\n[Please enter a number between 1 and 3 to select difficulty]")

                game_board.create_board()
            except ValueError:
                print("\n[Please enter a number between 1 and 3 to select difficulty]")
                difficulty = 0

        self.total_mines = total_mines
        self.difficulty = difficulty
        self.game_board = game_board
        self.start_time = time.time()

        self.game_loop() # Starts running the main game loop



    def game_loop(self):
        global game_over
        while(not(game_over)): 

            print("\n\n")


            count = 0
            for i in range(len(self.game_board.grid)):
                    for j in range(len(self.game_board.grid[0])):
                        if self.game_board.grid[i][j] == -1 and self.game_board.display_grid[i][j] == "F": # Check total number of unflagged mines left
                            count += 1
            print("\n[There are", self.total_mines - count,"unflagged mines left]\n")

            self.game_board.print_board()

            
            try:
                action = int(input("\nChoose action: [1] Open\n               [2] Flag\n               [3] Hint\n\n>")) # User action
                if (action > 0 and action <= 2):


                    while(True):   
                        try:
                            coords = input("\n[Enter X and Y coordinates in the format: >X Y]\n\n>")
                            x,y = int(coords.split(" ")[0]),int(coords.split(" ")[1]) # splits x and y coords from user input


                            if x-1 >= 0  and  x <= len(self.game_board.grid[0])  and y-1 >= 0  and  y <= len(self.game_board.grid):  # Checks if in bounds of grid
                                self.game_board.game_play(action,x-1,len(self.game_board.grid)-y)
                                break


                            else:
                                print("\n[Please enter valid coordinates]")
                        except (IndexError, ValueError) as e:
                            print("\n[Please enter valid coordinates]")

                elif action == 3:
                    self.game_board.game_play(action,1,1)

                else:
                    print("\n[Please enter 1 or 3 to confirm action]")
            except ValueError:
                print("\n[Please enter 1 or 3 to confirm action]")

        self.end_game_sequence()



    def end_game_sequence(self):
        if game_won:
            print("\n\n")
            self.game_board.print_board()
            print("\n[YOU WIN!]")

            end_time = round(time.time() - self.start_time,2)
            print("[Your time was", end_time,"]")
            name = str(input("\nEnter your name: "))

            if self.difficulty == 1:
                self.difficulty = "Beginner"
            elif self.difficulty == 2:
                self.difficulty = "Intermediate"
            elif self.difficulty == 3:
                self.difficulty = "Expert"

            person = str(end_time) + " " + self.difficulty + " " + name # save data of current player


            leaderboard = open("highscore.txt","r+")

            player_list = []
            for line in leaderboard:
                if line != "":
                    player_list.append(line[:-1])  # reads all scores from file into an array (and removes the \n)

            leaderboard.truncate(0) # reset the list
            

            new_player_list = []
            if len(player_list) == 0: # edge case when the leaderboard is empty
                with open("highscore.txt", "a") as file:
                    new_player_list.append(person)


            else:
                for i in range(len(player_list)):

                    if end_time < float(player_list[i].split()[0]): # saves scores when player beats a score
                        new_player_list.append(person)
                        for j in range(i,len(player_list)):
                            new_player_list.append(player_list[j])
                        break


                    elif i == len(player_list)-1:  # saves scores when a player is bottom of leaderboard
                        new_player_list.append(player_list[i])
                        new_player_list.append(person)

                    else:  #  saves scores when player does not beat a score
                        new_player_list.append(player_list[i])

                
            
            with open("highscore.txt", "a") as file:
                    for line in new_player_list:
                            file.write(line + "\n") # saves array of scores


            leaderboard.close() # saves file
            print("[Your score has been recorded in highscores.txt]")




        else:    # player loses
            for j in range(len(self.game_board.grid)):
                for i in range(len(self.game_board.grid[0])):
                    if self.game_board.grid[j][i] == -1 and self.game_board.display_grid[j][i] != "F":
                        self.game_board.display_grid[j][i] = "*"

            print("\n\n")
            self.game_board.print_board()
            print("\n[GAME OVER]")
            print("[YOU LOSE]")






# Start Game
print("Welcome to Minesweeper!")
new_game = game(0)
