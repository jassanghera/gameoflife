import time
import os
import next_state as ns
from board import dead_state, random_state, render

# -----------------------------------------------------------------------------
# Game of Life
# -----------------------------------------------------------------------------

# runs infinite loop of states, printing each iteration
def life(current_state):

    generation = 0

    try: 
        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"Generation: {generation}\n")
            render(current_state)

            current_state = ns.next_board_state(current_state)
            generation += 1

            time.sleep(0.05)

    except KeyboardInterrupt:
        print(f"Game stopped at iteration {generation}.")
        print("Thanks for playing Conway's Game of Life!\n")
        

# -----------------------------------------------------------------------------
# Pattern Loader
# -----------------------------------------------------------------------------

# represent patterns as a list of live cell coordinates (row, col) relative to an origin (0,0)
PATTERNS = {
    # Classic 3x3 glider (moves diagonally)
    "glider": [
        (0, 1),
        (1, 2),
        (2, 0), (2, 1), (2, 2),
    ],
    # Simple oscillator (period 2)
    "blinker": [
        (0, 0), (0, 1), (0, 2),
    ],
    # Another oscillator (period 2)
    "toad": [
        (0,1), (0,2), (0,3),
        (1,0), (1,1), (1,2),
    ],
    # still life, doesnt change
    "block": [
        (0,0), (0,1),
        (1,0), (1,1)
    ],
}

def stamp_pattern(state, cells, top, left):
    """
    Turn on cells in 'state' at positions offset by (top, left), 
    ignoring any cells that would fall out of bounds (bounded board)
    """

    height = len(state)
    width = len(state[0])

    for dr, dc in cells:
        r = top + dr
        c = left + dc
        if 0 <= r < height and 0 <= c < width:
            state[r][c] = 1

def board_with_pattern(width, height, pattern_name):
    """Create a new board with a pattern centered on it."""
    state = dead_state(width, height)

    cells = PATTERNS.get(pattern_name)
    if cells is None:
        raise ValueError(f"Unknown pattern: {pattern_name}")

    # Calculate top-left corner to center the pattern
    max_r = max(r for r, _ in cells)
    max_c = max(c for _, c in cells)
    pattern_height = max_r + 1
    pattern_width = max_c + 1

    top = (height - pattern_height) // 2
    left = (width - pattern_width) // 2

    stamp_pattern(state, cells, top, left)
    return state

def choose_pattern():
    options = ["random"] + list(PATTERNS.keys())
    print("Choose a starting configuration:")
    for i, name in enumerate(options, start=1):
        print(f'{i}. {name}')
    
    choice = input("Enter the number of your choice (or press Enter for random board): ").strip()

    if choice == "":
        return "random"  # default pattern
    
    if choice.isdigit():
        index = int(choice)
        if 1 <= index <= len(options):
            return options[index - 1]
        
    print("Invalid choice, defaulting to random.")
    return "random"

def make_initial_state(width, height, selection):
    if selection == "random":
        return random_state(width, height)
    return board_with_pattern(width, height, selection)

# -----------------------------------------------------------------------------
# main function
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    width, height = 25, 25

    selection = choose_pattern()
    state = make_initial_state(width, height, selection)

    life(state)