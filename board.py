import random

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
def random_state(width, height, p_alive=0.30):

    if not (0.0 <= p_alive <= 1.0):
        raise ValueError("p_alive must be between 0.0 and 1.0")
    

    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            state[i][j] = 1 if random.random() < p_alive else 0
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