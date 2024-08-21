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

            if random_number >= 0.2:
                cell_state = " "
            else:
                cell_state = '#'
            
            state[i][j] = cell_state
    
    return state


# this function prints the board neatly in the terminal
def render(state):

    for i in range(len(state)):
        print(*state[i])


#def next_board_state(state):
    # To Do: write a function to calculate the next state of the bord given an existing board


# FUNCTION CALLS FOR TESTING
#print(dead_state(4,5))
#print(random_state(3,4))
#render(random_state(3,4))
render(random_state(12,12))


