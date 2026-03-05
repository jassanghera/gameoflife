import random
import time
import os
import next_state as ns


# -----------------------------------------------------------------------------
# Board generation and rendering
# -----------------------------------------------------------------------------

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
    # Choose your characters
    # ALIVE = "█"   # or "⬛"
    ALIVE = "⬛"
    DEAD  = " "   # blank space

    for row in state:
        line = "".join(ALIVE if cell else DEAD for cell in row)
        print(line)

# -----------------------------------------------------------------------------
# Game of Life
# -----------------------------------------------------------------------------

# runs infinite loop of states, printing each iteration
def life(current_state):

    i = 0
    while i < 100:

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Iteration: ", i)
        render(current_state)

        current_state = ns.next_board_state(current_state)
        time.sleep(0.05)

        i += 1
    

    


# UNIT TESTS ---------------------------------------------------------------------------------

# if __name__ == "__main__":

#     # TEST 1: dead cells with no live neighbours should stay dead
#     init_state1 = [
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]
#     expected_next_state1 = [
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]

#     actual_next_state1 = next_board_state(init_state1)

#     if expected_next_state1 == actual_next_state1:
#         print("PASSED 1")
#     else:
#         print("FAILED 1")
#         print("Expected: ")
#         print(expected_next_state1)
#         print("Actual:")
#         print(actual_next_state1)

    
#     # TEST 2: dead cells with exactly 3 neighbours should come alive
#     init_state2 = [
#         [0,0,1],
#         [0,1,1],
#         [0,0,0]
#     ]
#     expected_next_state2 = [
#         [0,1,1],
#         [0,1,1],
#         [0,0,0]
#     ]
#     actual_next_state2 = next_board_state(init_state2)

#     if expected_next_state2 == actual_next_state2:
#         print("PASSED 2")
#     else:
#         print("FAILED 2!")
#         print("Expected:")
#         print(expected_next_state2)
#         print("Actual:")
#         print(actual_next_state2)
    
#     # TEST 3: dead cells with less than 3 neighbours stay dead, 
#     # live cells with less than 2 neighbours die
#     init_state3 = [
#         [1,0,0],
#         [0,1,0],
#         [0,0,0]
#     ]
#     expected_next_state3 = [
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]
#     actual_next_state3 = next_board_state(init_state3)

#     if expected_next_state3 == actual_next_state3:
#         print("PASSED 3")
#     else:
#         print("FAILED 3!")
#         print("Expected:")
#         print(expected_next_state3)
#         print("Actual:")
#         print(actual_next_state3)

#     # TEST 4: live cells with 2 or 3 neighbours continue to live 
#     init_state4 = [
#         [1,1,0],
#         [1,1,0],
#         [0,0,0]
#     ]
#     expected_next_state4 = [
#         [1,1,0],
#         [1,1,0],
#         [0,0,0]
#     ]
#     actual_next_state4 = next_board_state(init_state4)

#     if expected_next_state4 == actual_next_state4:
#         print("PASSED 4")
#     else:
#         print("FAILED 4!")
#         print("Expected:")
#         print(expected_next_state4)
#         print("Actual:")
#         print(actual_next_state4)

#     # TEST 5: live cells with 24 or more neighbours die 
#     init_state5 = [
#         [1,1,0],
#         [1,1,0],
#         [1,0,0]
#     ]
#     expected_next_state5 = [
#         [1,1,0],
#         [0,0,0],
#         [1,1,0]
#     ]
#     actual_next_state5 = next_board_state(init_state5)

#     if expected_next_state5 == actual_next_state5:
#         print("PASSED 5")
#     else:
#         print("FAILED 5!")
#         print("Expected:")
#         print(expected_next_state5)
#         print("Actual:")
#         print(actual_next_state5)

# COOL STATES --------------------------------------------------------------------------------


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


    # Initialize the starting state (example: a simple glider pattern)
glider =       [[0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]


# FUNCTION CALLS FOR TESTING -------------------------------------------------------------------------

life(random_state(20,20))
# life(random_state(25,25))
# life(random_state(40,40))
# life(gun_state)
# life(glider)