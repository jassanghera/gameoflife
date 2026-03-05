# a function to calculate the next state of the board given an existing board
def next_board_state(state):

    height = len(state) 
    width = len(state[0])

    new_state = dead_state(width, height)

    row_index = height - 1
    col_index = width - 1

    # iterate over cells, separate cases for edge cells(5 neighbours), corner cells(3 neighbours), and interior cells(8 neighbours)
    for i in range(height):
        for j in range(width):

            msg = " "
            neighbour_count = 0

            # EDGE CELLS (EXCLUDING CORNERS)
            # case 1: cell in first column, exclude top and bottom left corners
            if j == 0 and i != 0 and i != row_index:
                for x in range(j,j+2):
                    for y in range(i-1,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1
            
            # case 2: cell in last column, exclude top and bottom right corners
            elif j == col_index and i != 0 and i != row_index:
                for x in range(j-1,j+1):
                    for y in range(i-1,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1
            
            # case 3: cell in first row, exclude top left and right corners
            elif i == 0 and j != 0 and j != col_index:
                for x in range(j-1,j+2):
                    for y in range(i,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1

            # case 4: cell in last row, exclude bottom left and right corners
            elif i == row_index and j != 0 and j != col_index:
                for x in range(j-1,j+2):
                    for y in range(i-1,i+1):
                        if state[y][x] == 1:
                            neighbour_count += 1

            # CORNER CELLS
            # case 5: upper left corner
            elif i == 0 and j == 0:
                for x in range(j,j+2):
                    for y in range(i,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1
                            msg = "upper left corner"
            
            # case 6: upper right corner
            elif i == 0 and j == col_index:
                for x in range(j-1,j+1):
                    for y in range(i,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1
                            msg = "upper right corner"

            # case 7: bottom left corner
            elif i == row_index and j == 0:
                for x in range(j,j+2):
                    for y in range(i-1,i+1):
                        if state[y][x] == 1:
                            neighbour_count += 1
                            msg = "bottom left corner"

            # case 8: bottom right corner
            elif i == row_index and j == col_index:
                for x in range(j-1,j+1):
                    for y in range(i-1,i+1):
                        if state[y][x] == 1:
                            neighbour_count += 1
                            msg = "bottom right corner"

            # INTERIOR CELLS
            # case 9: interior cells
            else:
                for x in range(j-1,j+2):
                    for y in range(i-1,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1
            
            # if live cell, subtract it out from the neighbour count
            if state[i][j] == 1:
                neighbour_count -= 1
            
            #print("Cell " + "(", i, ",", j, ")" + ": ", neighbour_count, " ", msg)

            if state[i][j] == 1:
                if neighbour_count < 2 or neighbour_count >= 4:     # live cells with 0 or 1 neighbours die
                    new_state[i][j] = 0                             # # live cells with more than 3 neighbours die    
                else:
                    new_state[i][j] = state[i][j]                   # live cells with 2 or 3 neighbours continue to live
            else:
                if neighbour_count == 3:                            # dead cells with exactly 3 neighbours become alive
                    new_state[i][j] = 1
                else:                                               # all other dead cells continue to stay dead - new state unchanged
                    new_state[i][j] = state[i][j]
            
    return new_state