import random

print("hello life")

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
        print(state[i])


#def next_board_state(state):
    # To Do: write a function to calculate the next state of the bord given an existing board


# FUNCTION CALLS FOR TESTING
#print(dead_state(4,5))
#print(random_state(3,4))
#render(random_state(3,4))
render(random_state(12,12))

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