import random

print("hello world, i am life")
print("\n")

# dead_state should accept integer width and height
    #output: 2D grid as list of lists with all entries defaulted to 0
def dead_state(width, height):

    dead_board = []

    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        dead_board.append(row)

    return dead_board

# this function generates a random board with live cells = 1 and dead cells = 0
# input a default board (with all cells set to 0), output the randomized board
def random_state(width, height):

    state = dead_state(width, height)

    for i in range(height):
        for j in range(width):

            random_number = random.random()

            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            
            state[i][j] = cell_state
    
    return state


# this function prints the board neatly in the terminal
def render(state):

    for i in range(len(state)):
        print(*state[i])
    print("\n")


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
                            msg = "case 1"
            
            # case 2: cell in last column, exclude top and bottom right corners
            elif j == col_index and i != 0 and i != row_index:
                for x in range(j-1,j+1):
                    for y in range(i-1,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1
            
            # case 3: cell in first row, exclude top left and right corners
            elif i == 1 and j != 0 and j != col_index:
                for x in range(j-1,j+2):
                    for y in range(i,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1

            # case 4: cell in last row, exclude bottom left and right corners
            elif i == row_index and j != 0 and j != row_index:
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
            
            
            
            # minus 1 from neighbour count of all lives cells
            if neighbour_count > 0:
                neighbour_count -= 1
            
            print("Cell " + "(", i, ",", j, ")" + ": ", neighbour_count, " ", msg)

            # if state[i][j] == 1:
            #     if neighbour_count < 2:     # live cells with 0 or 1 neighbours die
            #         new_state[i][j] = 0     
            #     elif neighbour_count >= 4:  # live cells with more than 3 neighbours die
            #         new_state[i][j] = 0
            # elif state[i][j] == 0:
            #     if neighbour_count == 3:    # dead cells with exactly 3 neighbours become alive
            #         new_state[i][j] = 1
            # else:                           # live cells with 2 or 3 neighbours continue to live, dead cells continue to stay dead - new state unchanged
            #     new_state[i][j] = state[i][j]
            

    # return render(new_state)






# FUNCTION CALLS FOR TESTING
#print(dead_state(4,5))
#print(random_state(3,4))
#render(random_state(3,4))
#render(random_state(12,12))

test_state = random_state(5,5)

print("STATE: ")
render(test_state)
print("NEXT STATE: ")
next_board_state(test_state)


# COOL STATES

# STILL LIFE
# Canoe state 7x7 : Creates a still life canoe
canoe_state = [[0,0,0,0,0,0,0],
               [0,0,0,0,1,1,0],
               [0,0,0,0,0,1,0],
               [0,0,0,0,1,0,0],
               [0,1,0,1,0,0,0],
               [0,1,1,0,0,0,0],
               [0,0,0,0,0,0,0]]

# Block state 4x4 : is block
block_state = [[0,0,0,0],
               [0,1,1,0],
               [0,1,1,0],
               [0,0,0,0]]

# boat state 5x5 : not better than a canoe
boat_state = [[0,0,0,0,0],
              [0,1,1,0,0],
              [0,1,0,1,0],
              [0,0,1,0,0],
              [0,0,0,0,0]]

# Oscillators

# Beacon state : wee woo
beacon_state = [[0,0,0,0,0,0],
                [0,1,1,0,0,0],
                [0,1,1,0,0,0],
                [0,0,0,1,1,0],
                [0,0,0,1,1,0],
                [0,0,0,0,0,0]]

# Toad state : ribbit
toad_state =   [[0,0,0,0,0,0,],
                [0,0,0,1,0,0,],
                [0,1,0,0,1,0,],
                [0,1,0,0,1,0,],
                [0,0,1,0,0,0,],
                [0,0,0,0,0,0,]]

# Gun states

# GUN GUN GUN GUN GUN GUN GUN GUN PEW PEW BOOOOOOOOOOOOM
gun_state   = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
               [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]